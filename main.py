from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt
from stack import Stack
from constants import *

class Input:
    @staticmethod
    def integer(query: str):
        while True:
            try:
                n = int(input(query))
            except TypeError:
                print("Invalid input! Try again")
            else:
                break

        return n


class QCircuit:
    def __init__(self, *args):
        self.qc = QuantumCircuit(*args)
        self.num_qubits = args[0]
        self.gate_mappings = {
            "X": self.qc.x,
            "Y": self.qc.y,
            "H": self.qc.h,
            "Z": self.qc.z,
            "S": self.qc.s,
            "T": self.qc.t,
            "I": self.qc.id,
            "CX": self.qc.cx,
            "SWAP": self.qc.swap,
            "CSWAP": self.qc.cswap,
            "CCX": self.qc.ccx,
        }

        self.__stack = Stack()

    def __parse_string(self, string: str) -> tuple[str, list]:
        if len(string) == 0:
            raise ValueError("Nothing to parse - Query is empty!")

        gate, *qubits = string.split()
        gate = gate.upper()
        qubits = list(map(lambda x: int(x), qubits))

        return gate, qubits

    def create_circuit_from_file(self, file_name: str):
        with open(file_name, "r") as file:
            for line in file:
                query = line.strip()
                if not query:
                    continue
                gate, qubits = self.__parse_string(query)
                self.gate_mappings[gate](*qubits)

    def __is_valid_query(
        self, gate: str, qubits: list[int], valid_gates: dict[str, int]
    ):
        print(gate, qubits, valid_gates[gate])
        return gate.upper() in valid_gates and len(qubits) == valid_gates[gate]

    def encrypt(self, file_name: str):
        encryptors = {"X": 1, "CX": 2, "SWAP": 2, "CSWAP": 3, "CCX": 3}

        with open(file_name, "r") as file:
            for line in file:
                query = line.strip()
                if not query:
                    break
                gate, qubits = self.__parse_string(query)
                if self.__is_valid_query(gate, qubits, encryptors):
                    self.__stack.push((gate, qubits))
                    self.gate_mappings[gate](*qubits)

    def decrypt(self, incorrect_measure: str) -> str:
        stack = self.__stack
        if stack.empty():
            raise Exception(
                "Encryption not done! Encrypt your circuit first to apply decryption"
            )

        bits = [int(x) for x in incorrect_measure]

        while not stack.empty():
            quantum_gate, pos = stack.top()
            stack.pop()

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
            
            elif quantum_gate == 'X':
                bit = pos[0]
                bits[bit] ^= 1

            else:
                raise Exception("Unknown Error!!")

        return "".join([str(x) for x in bits])

    def measure(self):
        self.qc.measure_all()

    def draw(self, output="mpl", **kwargs):
        self.qc.draw(output=output, **kwargs)
        plt.show()

    def compile_and_run(self, shots=1024):
        simulator = AerSimulator()
        transpiled = transpile(self.qc, simulator)
        result = simulator.run(transpiled, shots=shots).result()
        return transpiled, result.get_counts()

    def create_circuit_from_terminal(self):
        while True:
            print(f"Available gates: {list(self.gate_mappings.keys())}")
            gate = input("Enter the gate to apply (or type 'done' to finish): ").upper()
            if gate == "DONE":
                break

            if gate in ["X", "Y", "H", "Z", "S", "T", "I"]:
                qubit = int(
                    input(
                        f"Enter the qubit (0 to {self.num_qubits - 1}) for the {gate} gate: "
                    )
                )
                self.gate_mappings[gate](qubit)

            elif gate == "CX":
                control = int(
                    input(
                        f"Enter the control qubit (0 to {self.num_qubits - 1}) for the CX gate: "
                    )
                )
                target = int(
                    input(
                        f"Enter the target qubit (0 to {self.num_qubits - 1}) for the CX gate: "
                    )
                )
                self.gate_mappings[gate](control, target)

            elif gate == "CCX":
                control1 = int(
                    input(
                        f"Enter the control qubit (0 to {self.num_qubits - 1}) for the CCX gate: "
                    )
                )
                control2 = int(
                    input(
                        f"Enter the control qubit (0 to {self.num_qubits - 1}) for the CCX gate: "
                    )
                )
                target = int(
                    input(
                        f"Enter the target qubit (0 to {self.num_qubits - 1}) for the CCX gate: "
                    )
                )

                self.gate_mappings[gate](control1, control2, target)

            elif gate == "SWAP":
                q1 = int(input("Enter the first qubit: "))  # Handle edge cases
                q2 = int(input("Enter the second qubit: "))  # Handle edge cases
                self.gate_mappings[gate](q1, q2)

            elif gate == "CSWAP":
                control = int(
                    input(
                        f"Enter the control qubit (0 to {self.num_qubits - 1}) for the CSWAP gate: "
                    )
                )
                q1 = int(input("Enter the first target qubit: "))  # Handle edge cases
                q2 = int(input("Enter the second target qubit: "))  # Handle edge cases
                self.gate_mappings[gate](control, q1, q2)

            else:
                print("Invalid gate. Please choose from the available options.")


qc = QCircuit(3)
qc.create_circuit_from_file(CIRCUIT_FILE)
qc.draw()
qc.encrypt(CLASSICAL_FILE)
qc.measure()
qc.draw()
transpiled, result = qc.compile_and_run()
print(result)

for incorrect_string in result.keys():
    corrected_string = qc.decrypt(incorrect_string)
    print(f"{incorrect_string} --> {corrected_string}")
