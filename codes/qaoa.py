import rustworkx as rx
from rustworkx.visualization import mpl_draw as draw_graph
import numpy as np
import matplotlib.pyplot as plt
from qiskit.quantum_info import SparsePauliOp
from qiskit.circuit.library import QAOAAnsatz
from scipy.optimize import minimize
from qiskit import transpile
from qiskit.primitives import StatevectorEstimator
from qiskit_ibm_runtime import SamplerV2 as Sampler
from typing import Sequence
from qiskit_aer import AerSimulator

# Code is taken as is from IBM Qiskit Learning and modified in structure to fit with our framework
# https://learning.quantum.ibm.com/tutorial/quantum-approximate-optimization-algorithm


class QAOA:
    def __init__(self, n: int, adjacency_list: list[tuple[int, int, float]]):
        self.num_qubits = n
        self.graph = rx.PyGraph()
        self.graph.add_nodes_from(range(n))
        self.graph.add_edges_from(adjacency_list)

    def plot_graph(self, node_size=600, with_labels=True, **kwargs):
        # draw_graph(self.graph, node_size=600, with_labels=True)
        draw_graph(self.graph, node_size=node_size, with_labels=with_labels, **kwargs)
        plt.show()

    def __build_max_cut_paulis(self) -> list[tuple[str, float]]:
        pauli_list = []
        for edge in list(self.graph.edge_list()):
            paulis = ["I"] * len(self.graph)
            paulis[edge[0]], paulis[edge[1]] = "Z", "Z"

            weight = self.graph.get_edge_data(edge[0], edge[1])

            pauli_list.append(("".join(paulis)[::-1], weight))

        return pauli_list

    def __cost_function_hamiltonian(
        self, max_cut_paulis: list[tuple[str, float]]
    ) -> SparsePauliOp:
        return SparsePauliOp.from_list(max_cut_paulis)

    def create_circuit(self, reps: int, measure_all: bool = True):
        max_cut_paulis = self.__build_max_cut_paulis()
        self.cost_hamiltonian = self.__cost_function_hamiltonian(max_cut_paulis)
        circuit = QAOAAnsatz(cost_operator=self.cost_hamiltonian, reps=reps)

        if measure_all:
            circuit.measure_all()

        return circuit

    def draw(self, circuit, output="mpl", **kwargs):
        circuit.draw(output=output, **kwargs)
        plt.show()

    def __compile_circuit(self, circuit, backend):
        transpiled = transpile(circuit, backend)
        return transpiled

    def compile_and_run_circuit(self, circuit, backend, reps: int, cost_hamiltonian):
        transpiled = self.__compile_circuit(circuit, backend)
        transpiled_no_meas = transpiled.remove_final_measurements(inplace=False)
        initial_gamma = np.pi
        initial_beta = np.pi / 2
        init_params = [initial_gamma, initial_beta] * reps

        objective_func_vals = []
        estimator = StatevectorEstimator()

        def cost_func_estimator(params, ansatz, hamiltonian, estimator):
            bound_circuit = ansatz.assign_parameters(params)
            # StatevectorEstimator expects a list of (circuit, observable) tuples
            pub = [(bound_circuit, hamiltonian)]
            job = estimator.run(pub)
            results = job.result()
            cost = results[0].data.evs  # Access expectation value from V2 result
            objective_func_vals.append(cost)
            return cost

        result = minimize(
            cost_func_estimator,
            init_params,
            args=(transpiled_no_meas, cost_hamiltonian, estimator),
            method="COBYLA",
            tol=1e-2,
        )

        return (
            transpiled.assign_parameters(result.x),
            result,
            objective_func_vals,
        )

    def plot_optim_graph(self, objective_func_vals):
        plt.figure(figsize=(12, 6))
        plt.plot(objective_func_vals)
        plt.xlabel("Iteration")
        plt.ylabel("Cost")
        plt.show()

    def get_distribution(self, transpiled_circuit, backend):
        sampler = Sampler(mode=backend)
        pub = transpiled_circuit
        job = sampler.run([pub], shots=int(1e4))
        counts_int = job.result()[0].data.meas.get_int_counts()
        counts_bin = job.result()[0].data.meas.get_counts()
        shots = sum(counts_int.values())
        final_distribution_int = {key: val / shots for key, val in counts_int.items()}
        final_distribution_bin = {key: val / shots for key, val in counts_bin.items()}
        return final_distribution_int, final_distribution_bin

    def to_bitstring(self, integer, num_bits):
        result = np.binary_repr(integer, width=num_bits)
        return [int(digit) for digit in result]

    def get_result(self, int_dist):
        keys = list(int_dist.keys())
        values = list(int_dist.values())
        most_likely = keys[np.argmax(np.abs(values))]
        most_likely_bitstring = self.to_bitstring(most_likely, len(self.graph))
        most_likely_bitstring.reverse()
        return most_likely_bitstring

    def plot_histogram(self, binary_dist):
        import matplotlib.pyplot as plt
        import matplotlib

        matplotlib.rcParams.update({"font.size": 10})
        # final_bits = final_distribution_bin
        values = np.abs(list(binary_dist.values()))
        top_4_values = sorted(values, reverse=True)[:4]
        positions = []
        for value in top_4_values:
            positions.append(np.where(values == value)[0])
        fig = plt.figure(figsize=(11, 6))
        ax = fig.add_subplot(1, 1, 1)
        plt.xticks(rotation=45)
        plt.title("Result Distribution")
        plt.xlabel("Bitstrings (reversed)")
        plt.ylabel("Probability")
        ax.bar(list(binary_dist.keys()), list(binary_dist.values()), color="tab:grey")
        for p in positions:
            ax.get_children()[int(p)].set_color("tab:purple")  # type: ignore
        plt.show()

    def evaluate_sample(self, x: Sequence[int], graph: rx.PyGraph) -> float:
        assert len(x) == len(
            list(graph.nodes())
        ), "The length of x must coincide with the number of nodes in the graph."
        return sum(
            x[u] * (1 - x[v]) + x[v] * (1 - x[u]) for u, v in list(graph.edge_list())
        )


if __name__ == "__main__":
    adjacency_list = [
        (0, 1, 1.0),
        (0, 2, 1.0),
        (0, 4, 1.0),
        (1, 2, 1.0),
        (2, 3, 1.0),
        (3, 4, 1.0),
    ]
    qaoa = QAOA(5, adjacency_list)
    qaoa.plot_graph()
    circuit_reps = 2
    circuit = qaoa.create_circuit(reps=circuit_reps)
    qaoa.draw(circuit)
    backend = AerSimulator()
    transpiled, result, objective_vals = qaoa.compile_and_run_circuit(
        circuit, backend, reps=circuit_reps, cost_hamiltonian=qaoa.cost_hamiltonian
    )
    print(result)
    qaoa.plot_optim_graph(objective_vals)
    int_dist, bin_dist = qaoa.get_distribution(transpiled, backend)

    ans = qaoa.get_result(int_dist)
    print(f"Ans = {ans}")
    qaoa.plot_histogram(bin_dist)
