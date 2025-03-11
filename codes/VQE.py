import matplotlib.pyplot as plt
from copy import deepcopy
import numpy as np
from qiskit.circuit.library import EfficientSU2
from qiskit.quantum_info import SparsePauliOp
from scipy.optimize import minimize
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit_ibm_runtime import EstimatorV2
from qiskit_ibm_runtime import SamplerV2


class VQE:
    def __init__(self, ansatz, hamiltonian, estimator, sampler):
        self.ansatz = ansatz
        self.hamiltonian = hamiltonian
        self.estimator = estimator
        self.sampler = sampler
        self.num_params: int = ansatz.num_parameters
        self.cost_history_dict = {
            "prev_vector": None,
            "iters": 0,
            "cost_history": [],
        }

        self.__ansatz_copy = deepcopy(ansatz)

    def get_uncompiled_ansatz(self):
        return self.__ansatz_copy

    def draw(self, ansatz, output="mpl", **kwargs):
        if output == "mpl":
            _, ax = plt.subplots()  # Create a new figure
            if "title" in kwargs:
                ax.set_title(kwargs["title"])  # Set title on the same figure
                kwargs.pop("title")
            ansatz.decompose().draw(
                output=output, ax=ax, **kwargs
            )  # Pass ax to use same figure
            plt.show()

    def __cost_func(self, params, ansatz):
        """Return estimate of energy from estimator

        Parameters:
            params (ndarray): Array of ansatz parameters
        Returns:
            float: Energy estimate
        """
        pub = (ansatz, [self.hamiltonian], [params])
        result = estimator.run(pubs=[pub]).result()  # type: ignore
        energy = result[0].data.evs[0]
        print("result from estimator: ", result[0].data.evs)
        self.cost_history_dict["iters"] += 1
        self.cost_history_dict["prev_vector"] = params
        self.cost_history_dict["cost_history"].append(energy)
        print(
            f"Iters. done: {self.cost_history_dict['iters']} [Current cost: {energy}]"
        )

        return energy

    def compile_ansatz(self, backend, optimization_level=3):
        return transpile(
            self.ansatz, backend=backend, optimization_level=optimization_level
        )

    def optimize(self, compiled_ansatz, method="cobyla", shots=10000):
        self.estimator.options.default_shots = shots
        self.sampler.options.default_shots = shots
        x0 = 2 * np.pi * np.random.random(self.num_params)
        res = minimize(
            self.__cost_func,
            x0,
            args=(compiled_ansatz),
            method=method,
        )

        return res

    def plot_optim_curve(self):
        _, ax = plt.subplots()
        ax.plot(
            range(self.cost_history_dict["iters"]),
            self.cost_history_dict["cost_history"],
        )
        ax.set_xlabel("Iterations")
        ax.set_ylabel("Cost")
        ax.set_title("Optimization plot")
        plt.show()
    
    def get_measurement_bitstrings(self, params, ansatz, shots=10000):
        """Get measurement bitstrings with their counts
        
        Parameters:
            params (ndarray): Array of ansatz parameters
            ansatz (QuantumCircuit): The ansatz circuit
            shots (int): Number of shots for sampling
            
        Returns:
            dict: Dictionary with bitstrings as keys and counts as values
        """
        self.sampler.options.default_shots = shots
        circuit = ansatz.assign_parameters(params)
        
        # Add measurements
        meas_circuit = circuit.copy()
        meas_circuit.measure_all()
        
        pub = (meas_circuit,)
        result = self.sampler.run(pubs=[pub]).result()
        counts = result[0].data.meas.get_counts()
        
        return counts


if __name__ == "__main__":
    hamiltonian = SparsePauliOp.from_list(
        [("YZ", 0.3980), ("ZI", -0.3980), ("ZZ", -0.0113), ("XX", 0.1810)]
    )
    ansatz = EfficientSU2(hamiltonian.num_qubits)
    backend = AerSimulator()
    estimator = EstimatorV2(mode=backend)
    sampler = SamplerV2(mode=backend)
    vqe = VQE(ansatz, hamiltonian, estimator, sampler)
    vqe.draw(ansatz, title="Ansatz before compiling")
    compiled = vqe.compile_ansatz(backend, optimization_level=3)
    result = vqe.optimize(compiled)
    print(result)
    vqe.plot_optim_curve()
    
    bitstrings_counts = vqe.get_measurement_bitstrings(result.x, compiled)
    print("\nMeasurement bitstrings and counts:")
    for bitstring, count in bitstrings_counts.items():
        print(f"Bitstring: {bitstring}, Count: {count}")
