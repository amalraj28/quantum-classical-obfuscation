from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt
from constants import *
from dequeue import Deque
from helper import read_qasm2, read_qasm3, write_qasm2, write_qasm3

class QCircuit:
    def __init__(self, *args, from_qasm=True):
        self.qc = args[0] if from_qasm else QuantumCircuit(*args)
        self.num_qubits = self.qc.num_qubits
        self.gate_mappings = {
            "X": self.qc.x,
            "Y": self.qc.y,
            "H": self.qc.h,
            "Z": self.qc.z,
            "S": self.qc.s,
            "T": self.qc.t,
            "I": self.qc.id,
            "CX": self.qc.cx,
            "CY": self.qc.cy,
            "CZ": self.qc.cz,
            "SWAP": self.qc.swap,
            "CSWAP": self.qc.cswap,
            "CCX": self.qc.ccx,
        }

        self.__deque = Deque()
        
    @classmethod
    def from_qasm2(cls, file_name: str):
        qc = read_qasm2(file_name)
        return cls(qc)
    
    @classmethod
    def from_qasm3(cls, file_name: str):
        qc = read_qasm3(file_name)
        return cls(qc)
    
    def __parse_string(self, string: str) -> tuple[str, list[int]]:
        if len(string) == 0:
            raise ValueError("Nothing to parse - Query is empty!")

        gate, *qubits = string.split()
        gate = gate.upper()
        qubits = list(map(lambda x: int(x), qubits))

        return gate, qubits

    def to_qasm2(self, file_name: str):
        write_qasm2(self.qc, file_name)
    
    def to_qasm3(self, file_name: str):
        write_qasm3(self.qc, file_name)
    
    # def create_circuit_from_file(self, file_name: str):
    #     with open(file_name, "r") as file:
    #         for line in file:
    #             query = line.strip()
    #             if not query:
    #                 continue
    #             gate, qubits = self.__parse_string(query)
    #             self.gate_mappings[gate](*qubits)

    def __is_valid_query(
        self, gate: str, qubits: list[int], valid_gates: dict[str, int]
    ):
        return gate.upper() in valid_gates and len(qubits) == valid_gates[gate]

    def encrypt(self, file_name: str):
        with open(file_name, "r") as file:
            for line in file:
                query = line.strip()
                if not query:
                    break
                gate, qubits = self.__parse_string(query)
                if self.__is_valid_query(gate, qubits, CLASSICAL_GATES):
                    self.gate_mappings[gate](*qubits)
                    bit_pos = list(map(lambda x: self.num_qubits - x - 1, qubits))
                    self.__deque.push_back((gate, bit_pos))

    def decrypt(self, incorrect_measure: str) -> str:
        deque = self.__deque

        if deque.empty():
            raise Exception(
                "Encryption not done! Encrypt your circuit first to apply decryption"
            )

        bits = [int(x) for x in incorrect_measure]

        n = deque.size()

        for _ in range(n):
            quantum_gate, pos = deque.back()
            deque.pop_back()
            deque.push_front((quantum_gate, pos))

            if quantum_gate == "CX":
                ctrl, target = pos
                bits[target] = bits[target] ^ bits[ctrl]

            elif quantum_gate == "CCX":
                c1, c2, t = pos
                bits[t] = (bits[c1] & bits[c2]) ^ bits[t]

            elif quantum_gate == "SWAP":
                bit1, bit2 = pos
                bits[bit2], bits[bit1] = (
                    bits[bit1],
                    bits[bit2],
                )

            elif quantum_gate == "CSWAP":
                ctrl, bit1, bit2 = pos
                if bits[ctrl] == 1:
                    bits[bit2], bits[bit1] = (
                        bits[bit1],
                        bits[bit2],
                    )

            elif quantum_gate == "X":
                bit = pos[0]
                bits[bit] ^= 1

            else:
                raise Exception("Unknown Error!!")

        return "".join([str(x) for x in bits])

    def measure(self, add_bits: bool = False):
        self.qc.measure_all(add_bits=add_bits)

    def draw(self, output="mpl", **kwargs):
        if output == 'text':
            print(self.qc.draw(output=output, **kwargs))
        else:
            self.qc.draw(output=output, **kwargs)
            plt.show()

    def compile_and_run(self, shots=1024):
        simulator = AerSimulator()
        transpiled = transpile(self.qc, simulator)
        result = simulator.run(transpiled, shots=shots).result()
        return transpiled, result.get_counts()

if __name__ == '__main__':
    # n = Input.integer('Enter the number of qubits: ')
    # qc = QCircuit(n, from_qasm=False)
    qc = QCircuit.from_qasm2('output.qasm')
    # qc = QCircuit.from_qasm3('output3.qasm')
    # qc.create_circuit_from_file(CIRCUIT_FILE)
    qc.draw()
    qc.encrypt(CLASSICAL_FILE)
    qc.draw()
    qc.measure()
    
    # qc.to_qasm3('output3.qasm')
    transpiled, result = qc.compile_and_run()
    print(result)

    for incorrect_string in result.keys():
        corrected_string = qc.decrypt(incorrect_string)
        print(f"{incorrect_string} --> {corrected_string}")
