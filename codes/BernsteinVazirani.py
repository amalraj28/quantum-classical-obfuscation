from qiskit import QuantumCircuit, QuantumRegister, AncillaRegister, ClassicalRegister
import matplotlib.pyplot as plt


class BernsteinVazirani:
    def __init__(self, secret_factor_bits: str, bias_bit: int):
        self.secret_factor_bits = secret_factor_bits
        self.total_qubits = len(self.secret_factor_bits) + 1
        self.bias_bit = bias_bit % 2
        self.qc = QuantumCircuit(
            QuantumRegister(self.total_qubits - 1, "q"),
            AncillaRegister(1, "a"),
            ClassicalRegister(self.total_qubits - 1, "c"),
        )

    def make_oracle(self) -> QuantumCircuit:
        oracle = QuantumCircuit(
            QuantumRegister(self.total_qubits - 1), AncillaRegister(1)
        )
        ancilla_qbit: int = self.total_qubits - 1
        n = len(self.secret_factor_bits)

        oracle.z(ancilla_qbit)
        if self.bias_bit:
            oracle.x(ancilla_qbit)

        for i in range(n):
            idx: int = n - i - 1
            if self.secret_factor_bits[idx] == "1":
                oracle.cx(i, ancilla_qbit)

        return oracle

    def create_circuit(self, add_measurement: bool = False) -> QuantumCircuit:
        self.qc.h(range(self.total_qubits))
        self.qc.barrier()
        self.qc.compose(self.make_oracle(), inplace=True)
        self.qc.barrier()
        self.qc.h(range(self.total_qubits - 1))

        if add_measurement:
            self.qc.measure(range(self.total_qubits - 1), range(self.total_qubits - 1))

        return self.qc

    def draw(self, output="mpl", **kwargs):
        if output == "text":
            print(self.qc.draw(output=output, **kwargs))
        
        else:
            self.qc.draw(output=output, **kwargs)
            plt.show()
    