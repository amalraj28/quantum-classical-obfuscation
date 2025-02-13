from itertools import chain
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt
from dequeue import Deque
from helper import *
import random


class QCircuit:
    def __init__(self, *args, from_qasm=True):
        self.qc = args[0] if from_qasm else QuantumCircuit(*args)
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

        self.gate_index = {
            0: "I",
            1: "X",
            2: "CX",
            3: "SWAP",
            4: "CCX",
            5: "CSWAP",
        }

        self.qubit_count = {"I": 1, "X": 1, "CX": 2, "SWAP": 2, "CCX": 3, "CSWAP": 3}

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

    def __is_valid_query(
        self, gate: str, qubits: list[int], valid_gates: dict[str, int]
    ):
        return gate.upper() in valid_gates and len(qubits) == valid_gates[gate]

    def encrypt(self, key_size: int) -> str:
        rem = key_size
        key: list[list[int]] = []
        n = self.qc.num_qubits

        while rem > 0:
            idx = random.randint(0, 5)
            gate = self.gate_index[idx]
            contr = self.qubit_count[gate] + 1
            if rem - contr == 0 or rem - contr > 1:
                encryptor: list[int] = []
                encryptor.append(idx)
                qubits = random.sample(range(n), contr - 1)
                self.gate_mappings[gate](*qubits)
                encryptor.extend(qubits)
                key.append(encryptor)
                rem -= contr

        flattened_list = list(map(lambda x: str(x), chain.from_iterable(key)))
        return "".join(flattened_list)

    def decrypt(self, key: str, incorrect_measure: str):
        deque = Deque()
        n = self.qc.num_qubits
        measurement = [int(x) for x in incorrect_measure]

        if len(measurement) == 0:
            raise ValueError("Not a valid measurement result!")

        i = 0

        while i < len(key):
            gate_idx = int(key[i])
            if gate_idx not in self.gate_index:
                raise ValueError(f"Invalid key {key}. Value at index {i+1} is invalid!")

            gate = self.gate_index[gate_idx]
            num_qubits = self.qubit_count[gate]
            qubits_as_str = key[i + 1 : i + 1 + num_qubits]
            deque.push_back((gate, qubits_as_str))
            i += 1 + num_qubits

        while not deque.empty():
            quantum_gate, qubits_string = deque.back()
            deque.pop_back()
            bit_pos = list(map(lambda x: n - int(x) - 1, qubits_string))

            if quantum_gate == "CX":
                ctrl, target = bit_pos
                measurement[target] = measurement[target] ^ measurement[ctrl]

            elif quantum_gate == "CCX":
                c1, c2, t = bit_pos
                measurement[t] = (measurement[c1] & measurement[c2]) ^ measurement[t]

            elif quantum_gate == "SWAP":
                bit1, bit2 = bit_pos
                measurement[bit2], measurement[bit1] = (
                    measurement[bit1],
                    measurement[bit2],
                )

            elif quantum_gate == "CSWAP":
                ctrl, bit1, bit2 = bit_pos
                if measurement[ctrl] == 1:
                    measurement[bit2], measurement[bit1] = (
                        measurement[bit1],
                        measurement[bit2],
                    )

            elif quantum_gate == "X":
                bit = bit_pos[0]
                measurement[bit] ^= 1

            elif quantum_gate == "I":
                continue

            else:
                raise Exception("Unknown error while decoding!")

        return ''.join(list(map(str, measurement)))

    def measure(self, add_bits: bool = False):
        self.qc.measure_all(add_bits=add_bits)

    def draw(self, output="mpl", **kwargs):
        if output == "text":
            print(self.qc.draw(output=output, **kwargs))
        else:
            self.qc.draw(output=output, **kwargs)
            plt.show()

    def compile_and_run(self, shots=1024):
        simulator = AerSimulator()
        transpiled = transpile(self.qc, simulator)
        result = simulator.run(transpiled, shots=shots).result()
        return transpiled, result.get_counts()


if __name__ == "__main__":
    qc = QCircuit.from_qasm2("output.qasm")
    qc.draw("text")
    key = qc.encrypt(20)
    qc.draw("text")
    qc.measure()

    transpiled, result = qc.compile_and_run()
    print(result)

    for incorrect_string in result.keys():
        corrected_string = qc.decrypt(key, incorrect_string)
        print(f"{incorrect_string} --> {corrected_string}")
