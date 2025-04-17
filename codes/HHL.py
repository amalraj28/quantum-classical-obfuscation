# Code taken from the below link and modified to fit into our framework
# https://github.com/hywong2/HHL_Example/blob/main/HHL_Hector_Wong.ipynb

from qiskit import QuantumCircuit, QuantumRegister, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import numpy as np
from matplotlib import pyplot as plt

class HHL:
    def __init__(
        self, clock_reg: int = 2, input_reg: int = 1, ancilla: int = 1
    ):
        self.clock = QuantumRegister(clock_reg, name="clock")
        self.input_reg = QuantumRegister(
            input_reg, name="b"
        )  
        self.ancilla = QuantumRegister(ancilla, name="ancilla")
        # self.measurement = ClassicalRegister(measure, name="c")
        self.qc = QuantumCircuit(
            self.ancilla, self.clock, self.input_reg
        )

    def qft_dagger(self, q, n):
        self.qc.h(self.clock[1])
        for j in reversed(range(n)):
            for k in reversed(range(j + 1, n)):
                # Replace cu1 with cp (controlled phase gate)
                self.qc.cp(-np.pi / float(2 ** (k - j)), q[k], q[j])
        self.qc.h(self.clock[0])
        self.qc.swap(self.clock[0], self.clock[1])

    def qft(self, q, n):
        self.qc.swap(self.clock[0], self.clock[1])
        self.qc.h(self.clock[0])
        for j in reversed(range(n)):
            for k in reversed(range(j + 1, n)):
                # Replace cu1 with cp
                self.qc.cp(np.pi / float(2 ** (k - j)), q[k], q[j])
        self.qc.h(self.clock[1])

    def qpe(self):
        self.qc.barrier()

        # Replace cu with explicit controlled unitary
        # e^{i*A*t}: Controlled-U with angles (theta, phi, lambda, gamma)
        self.qc.cu(
            np.pi / 2,
            -np.pi / 2,
            np.pi / 2,
            3 * np.pi / 4,
            self.clock[0],
            self.input_reg[0],
            label="U",
        )

        # e^{i*A*t*2}
        self.qc.cu(np.pi, np.pi, 0, 0, self.clock[1], self.input_reg[0], label="U2")

        self.qc.barrier()

        # Perform an inverse QFT on the register holding the eigenvalues
        self.qft_dagger(self.clock, 2)

    def inv_qpe(self):
        # Perform a QFT on the register holding the eigenvalues
        self.qft(self.clock, 2)

        self.qc.barrier()

        # e^{i*A*t*2}
        self.qc.cu(np.pi, np.pi, 0, 0, self.clock[1], self.input_reg[0], label="U2")

        # e^{i*A*t}
        self.qc.cu(
            np.pi / 2,
            np.pi / 2,
            -np.pi / 2,
            -3 * np.pi / 4,
            self.clock[0],
            self.input_reg[0],
            label="U",
        )

        self.qc.barrier()

    def hhl(self):
        self.qpe()

        self.qc.barrier()

        # This section is to test and implement C = 1
        self.qc.cry(np.pi, self.clock[0], self.ancilla[0])
        self.qc.cry(np.pi / 3, self.clock[1], self.ancilla[0])

        self.qc.barrier()

        # self.qc.measure(self.ancilla[0], self.measurement[0])
        self.qc.barrier()
        self.inv_qpe()

    def draw(self, output="mpl", **kwargs):
        self.qc.draw(output=output)
        if "title" in kwargs:
            plt.title(kwargs["title"])
        if output == "mpl":
            plt.show()

    def compile_and_run(self):
        simulator = AerSimulator()
        circuit_transpiled = transpile(self.qc, backend=simulator)
        result = simulator.run(circuit_transpiled, shots=65536).result()
        return result.get_counts(self.qc)

    def plot_counts(self, res):
        plot_histogram(res)
        plt.show()


# if __name__ == "__main__":
#     qc = HHL()
#     qc.qc.x(qc.input_reg)
#     qc.qc.h(qc.clock)
#     qc.hhl()
#     qc.qc.h(qc.clock)
#     qc.qc.measure(qc.input_reg[0], qc.measurement[1])
#     qc.draw(title="Circuit")
    
#     res = qc.compile_and_run()
#     qc.plot_counts(res)
