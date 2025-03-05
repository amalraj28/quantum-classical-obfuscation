import rustworkx as rx
from rustworkx.visualization import mpl_draw as draw_graph
import numpy as np
import matplotlib.pyplot as plt
from qiskit.quantum_info import SparsePauliOp
from qiskit.circuit.library import QAOAAnsatz

class QAOA:
    def __init__(self, n: int, adjacency_list: list[tuple[int, int, float]]):
        self.num_qubits = n
        self.graph = rx.PyGraph()
        self.graph.add_nodes_from(range(n))
        self.graph.add_edges_from(adjacency_list)
        
    def plot_graph(self, **kwargs):
        # draw_graph(self.graph, node_size=600, with_labels=True)
        draw_graph(self.graph, **kwargs)
        plt.show()
    
    def __build_max_cut_paulis(self) -> list[tuple[str, float]]:
        """Convert the graph to Pauli list.

        This function does the inverse of `build_max_cut_graph`
        """
        pauli_list = []
        for edge in list(self.graph.edge_list()):
            paulis = ["I"] * len(self.graph)
            paulis[edge[0]], paulis[edge[1]] = "Z", "Z"

            weight = self.graph.get_edge_data(edge[0], edge[1])

            pauli_list.append(("".join(paulis)[::-1], weight))

        return pauli_list
    
    def __cost_function_hamiltonian(self, max_cut_paulis: list[tuple[str, float]]) -> SparsePauliOp:
        return SparsePauliOp.from_list(max_cut_paulis)
    
    def create_circuit(self,  reps: int, measure_all: bool = True):
        max_cut_paulis = self.__build_max_cut_paulis()
        cost_hamiltonian = self.__cost_function_hamiltonian(max_cut_paulis)
        circuit = QAOAAnsatz(cost_operator=cost_hamiltonian, reps=reps)
        
        if measure_all:
            circuit.measure_all()
        
        return circuit
    
    def draw(self):
        pass
    
    
        
        
        

# n = 5

# graph = rx.PyGraph()
# graph.add_nodes_from(np.arange(0, n, 1))
# edge_list = [(0, 1, 1.0), (0, 2, 1.0), (0, 4, 1.0), (1, 2, 1.0), (2, 3, 1.0), (3, 4, 1.0)]
# graph.add_edges_from(edge_list)
# draw_graph(graph, node_size=600, with_labels=True)
# plt.show()

# def build_max_cut_paulis(graph: rx.PyGraph) -> list[tuple[str, float]]:
#     """Convert the graph to Pauli list.

#     This function does the inverse of `build_max_cut_graph`
#     """
#     pauli_list = []
#     for edge in list(graph.edge_list()):
#         paulis = ["I"] * len(graph)
#         paulis[edge[0]], paulis[edge[1]] = "Z", "Z"

#         weight = graph.get_edge_data(edge[0], edge[1])

#         pauli_list.append(("".join(paulis)[::-1], weight))

#     return pauli_list


# max_cut_paulis = build_max_cut_paulis(graph)

# cost_hamiltonian = SparsePauliOp.from_list(max_cut_paulis)
# print("Cost Function Hamiltonian:", cost_hamiltonian)


circuit.measure_all()

circuit.draw('mpl', interactive=True)
plt.show()

print(circuit.parameters)

objective_func_vals = []

# def cost_func_estimator(params, ansatz, hamiltonian, estimator):

#     # transform the observable defined on virtual qubits to
#     # an observable defined on all physical qubits
#     isa_hamiltonian = hamiltonian.apply_layout(ansatz.layout)

#     pub = (ansatz, isa_hamiltonian, params)
#     job = estimator.run([pub])

#     results = job.result()[0]
#     cost = results.data.evs

#     objective_func_vals.append(cost)

#     return cost

# from qiskit_ibm_runtime import Session, EstimatorV2 as Estimator
from scipy.optimize import minimize

objective_func_vals = [] # Global variable
# with Session(backend=backend) as session:
#     # If using qiskit-ibm-runtime<0.24.0, change `mode=` to `session=`
#     estimator = Estimator(mode=session)
#     estimator.options.default_shots = 1000

#     # Set simple error suppression/mitigation options
#     estimator.options.dynamical_decoupling.enable = True
#     estimator.options.dynamical_decoupling.sequence_type = "XY4"
#     estimator.options.twirling.enable_gates = True
#     estimator.options.twirling.num_randomizations = "auto"

#     result = minimize(
#         cost_func_estimator,
#         init_params,
#         args=(candidate_circuit, cost_hamiltonian, estimator),
#         method="COBYLA",
#         tol=1e-2,
#     )
#     print(result)

from qiskit_aer import AerSimulator
from qiskit.primitives import StatevectorEstimator
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
from scipy.optimize import minimize
import numpy as np

backend = AerSimulator()
pm = generate_preset_pass_manager(optimization_level=3, backend=backend)
candidate_circuit = pm.run(circuit)  # Assuming 'circuit' is defined
candidate_circuit_no_meas = candidate_circuit.remove_final_measurements(inplace=False)
initial_gamma = np.pi
initial_beta = np.pi/2
init_params = [initial_gamma, initial_beta, initial_gamma, initial_beta]
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

result = minimize(cost_func_estimator, init_params, args=(candidate_circuit_no_meas, cost_hamiltonian, estimator), method="COBYLA", tol=1e-2)
optimized_circuit = candidate_circuit_no_meas.assign_parameters(result.x)

print(result)

import matplotlib.pyplot as plt

plt.figure(figsize=(12, 6))
plt.plot(objective_func_vals)
plt.xlabel("Iteration")
plt.ylabel("Cost")
plt.show()

optimized_circuit = candidate_circuit.assign_parameters(result.x)
optimized_circuit.draw('mpl', fold=False, idle_wires=False)
plt.show()

from qiskit_ibm_runtime import SamplerV2 as Sampler

# If using qiskit-ibm-runtime<0.24.0, change `mode=` to `backend=`
sampler = Sampler(mode=backend)
# sampler.options.default_shots = 10000

# # Set simple error suppression/mitigation options
# sampler.options.dynamical_decoupling.enable = True
# sampler.options.dynamical_decoupling.sequence_type = "XY4"
# sampler.options.twirling.enable_gates = True
# sampler.options.twirling.num_randomizations = "auto"

pub= (optimized_circuit, )
job = sampler.run([pub], shots=int(1e4))
counts_int = job.result()[0].data.meas.get_int_counts()
counts_bin = job.result()[0].data.meas.get_counts()
shots = sum(counts_int.values())
final_distribution_int = {key: val/shots for key, val in counts_int.items()}
final_distribution_bin = {key: val/shots for key, val in counts_bin.items()}
print(final_distribution_int)

# auxiliary functions to sample most likely bitstring
def to_bitstring(integer, num_bits):
    result = np.binary_repr(integer, width=num_bits)
    return [int(digit) for digit in result]

keys = list(final_distribution_int.keys())
values = list(final_distribution_int.values())
most_likely = keys[np.argmax(np.abs(values))]
most_likely_bitstring = to_bitstring(most_likely, len(graph))
most_likely_bitstring.reverse()

print("Result bitstring:", most_likely_bitstring)

import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams.update({"font.size": 10})
final_bits = final_distribution_bin
values = np.abs(list(final_bits.values()))
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
ax.bar(list(final_bits.keys()), list(final_bits.values()), color="tab:grey")
for p in positions:
    ax.get_children()[int(p)].set_color("tab:purple")
plt.show()

# auxiliary function to plot graphs
def plot_result(G, x):
    colors = ["tab:grey" if i == 0 else "tab:purple" for i in x]
    pos, default_axes = rx.spring_layout(G), plt.axes(frameon=True)
    draw_graph(G, node_color=colors, node_size=100, alpha=0.8, pos=pos)


plot_result(graph, most_likely_bitstring)
plt.show()

from typing import Sequence
def evaluate_sample(x: Sequence[int], graph: rx.PyGraph) -> float:
    assert len(x) == len(list(graph.nodes())), "The length of x must coincide with the number of nodes in the graph."
    return sum(x[u] * (1 - x[v]) + x[v] * (1 - x[u]) for u, v in list(graph.edge_list()))


cut_value= evaluate_sample(most_likely_bitstring, graph)
print('The value of the cut is:', cut_value)