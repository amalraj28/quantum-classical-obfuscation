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


def create_circuit_from_file(file_name: str, qc: QuantumCircuit, gate_mappings):
    with open(file_name, "r") as file:
        for line in file:
            query = line.strip()
            if not query:
                break
            gate, qubits = parse_string(query)
            gate_mappings[gate](*qubits)

    return qc


def create_circuit(n: int):
    qc = QuantumCircuit(n)

    print("Available gates: X, H, CX (CNOT), Z, S, T, SWAP")
    gates = {
        "X": qc.x,
        "Y": qc.y,
        "H": qc.h,
        "Z": qc.z,
        "S": qc.s,
        "T": qc.t,
        "CX": qc.cx,
        "SWAP": qc.swap,
        "CSWAP": qc.cswap,
        "CCX": qc.ccx,
    }

    while True:
        gate = input("Enter the gate to apply (or type 'done' to finish): ").upper()
        if gate == "DONE":
            break

        if gate in ["X", "H", "Z", "S", "T"]:
            qubit = int(input(f"Enter the qubit (0 to {n - 1}) for the {gate} gate: "))
            gates[gate](qubit)

        elif gate == "CX":
            control = int(
                input(f"Enter the control qubit (0 to {n - 1}) for the CX gate: ")
            )
            target = int(
                input(f"Enter the target qubit (0 to {n - 1}) for the CX gate: ")
            )
            qc.cx(control, target)

        elif gate == "SWAP":
            q1 = int(input("Enter the first qubit: "))  # Handle edge cases
            q2 = int(input("Enter the second qubit: "))  # Handle edge cases
            gates[gate](q1, q2)

        else:
            print("Invalid gate. Please choose from the available options.")

    return qc


def compile_and_run(circuit: QuantumCircuit):
    simulator = AerSimulator()
    transpiled = transpile(circuit, simulator)
    result = simulator.run(transpiled, shots=1024).result()
    return transpiled, result.get_counts()


def draw(qc: QuantumCircuit, output="mpl"):
    qc.draw(output=output)
    plt.show()


def add_classical_gate(qc: QuantumCircuit, gate: str, qubits: list[int]):
    gate = gate.upper()
    gates = {
        "X": qc.x,
        "Y": qc.y,
        "H": qc.h,
        "Z": qc.z,
        "S": qc.s,
        "T": qc.t,
        "CX": qc.cx,
        "SWAP": qc.swap,
        "CSWAP": qc.cswap,
        "CCX": qc.ccx,
    }

    if gate not in ["CX", "CCX", "SWAP", "CSWAP"]:
        raise ValueError(f"Invalid gate {gate}")

    if gate in ["CX", "SWAP"]:
        if len(qubits) != 2:
            raise ValueError("Number of qubits must be exactly 2")

        gates[gate](*qubits)

    else:
        if len(qubits) != 3:
            raise ValueError("Number of qubits must be exactly 3")

        gates[gate](*qubits)

    return qc


def parse_string(string: str):
    if len(string) == 0:
        return

    gate, *qubits = string.split()
    gate = gate.upper()
    qubits = list(map(lambda x: int(x), qubits))

    return gate, qubits


def correct_measurement(
    stack: Stack, incorrect_string_list: list[int]
) -> list[int | None]:
    if stack.empty():
        return []

    correct_string_list = [int(x) for x in incorrect_string_list]

    while not stack.empty():
        quantum_gate, pos = stack.top()
        stack.pop()

        if quantum_gate == "CX":
            ctrl, target = pos
            correct_string_list[target] = (
                incorrect_string_list[target] ^ incorrect_string_list[ctrl]
            )

        elif quantum_gate == "CCX":
            c1, c2, t = pos
            correct_string_list[t] = (
                incorrect_string_list[c1] & incorrect_string_list[c2]
            ) ^ incorrect_string_list[t]

        elif quantum_gate == "SWAP":
            bit1, bit2 = pos
            correct_string_list[bit2], correct_string_list[bit1] = (
                incorrect_string_list[bit1],
                incorrect_string_list[bit2],
            )

        elif quantum_gate == "CSWAP":
            ctrl, bit1, bit2 = pos
            if incorrect_string_list[ctrl] == 1:
                correct_string[bit2], correct_string[bit1] = (
                    incorrect_string_list[bit1],
                    incorrect_string_list[bit2],
                )

        else:
            raise Exception("Unknown Error!!")

    return correct_string_list


def list_to_string(lst: list):
    string_list = [str(x) for x in lst]
    return "".join(string_list)


if __name__ == "__main__":
    # n = Input.integer("Enter the number of qubits: ")
    # qc = create_circuit(n)
    # valid_gates = ["CX", "CCX", "SWAP", "CSWAP"]
    # gate_operations = {
    #     "X": qc.x,
    #     "Y": qc.y,
    #     "H": qc.h,
    #     "Z": qc.z,
    #     "S": qc.s,
    #     "T": qc.t,
    #     "CX": qc.cx,
    #     "SWAP": qc.swap,
    #     "CSWAP": qc.cswap,
    #     "CCX": qc.ccx,
    # }

    # stack = Stack()

    # while True:
    #     prompt = input(
    #         "Enter the gates and qubit to be added at the end of circuit, separated by space (leave blank for exiting): "
    #     )
    #     if len(prompt) == 0:
    #         break

    #     gate, qubits = parse_string(prompt)
    #     qc = add_classical_gate(qc, gate, qubits)
    #     stack.push((gate, qubits))

    # qc.measure_all()
    # draw(qc)
    # transpiled, results = compile_and_run(qc)

    # incorrect_string_list = list(results.keys())[0]  # Assuming only a single output
    # incorrect_bits_list = [int(x) for x in incorrect_string_list]
    # print(f"Incorrect string = {incorrect_bits_list}")

    # correct_bits_list = correct_measurement(stack, incorrect_bits_list)

    # correct_string = list_to_string(correct_bits_list)
    # print(f"Correct string = {correct_string}")
    qc = QuantumCircuit(4)
    gate_operations = {
        "X": qc.x,
        "Y": qc.y,
        "H": qc.h,
        "Z": qc.z,
        "S": qc.s,
        "T": qc.t,
        "CX": qc.cx,
        "SWAP": qc.swap,
        "CSWAP": qc.cswap,
        "CCX": qc.ccx,
    }
    qc = create_circuit_from_file(CIRCUIT_FILE, qc, gate_operations)
    draw(qc)


class QCircuit:
    def __init__(self, *args):
        self.qc = QuantumCircuit(*args)
        self.num_qubits = args[0]
        self.gate_operations = {
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

    def __parse_string(self, string: str):
        if len(string) == 0:
            return

        gate, *qubits = string.split()
        gate = gate.upper()
        qubits = list(map(lambda x: int(x), qubits))

        return gate, qubits

    def create_circuit(self):
        while True:
            print(f"Available gates: {list(self.gate_operations.keys())}")
            gate = input("Enter the gate to apply (or type 'done' to finish): ").upper()
            if gate == "DONE":
                break

            if gate in ["X", "Y", "H", "Z", "S", "T", "I"]:
                qubit = int(
                    input(
                        f"Enter the qubit (0 to {self.num_qubits - 1}) for the {gate} gate: "
                    )
                )
                self.gate_operations[gate](qubit)

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
                self.gate_operations[gate](control, target)

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

                self.gate_operations[gate](control1, control2, target)

            elif gate == "SWAP":
                q1 = int(input("Enter the first qubit: "))  # Handle edge cases
                q2 = int(input("Enter the second qubit: "))  # Handle edge cases
                self.gate_operations[gate](q1, q2)

            elif gate == "CSWAP":
                control = int(
                    input(
                        f"Enter the control qubit (0 to {self.num_qubits - 1}) for the CSWAP gate: "
                    )
                )
                q1 = int(input("Enter the first target qubit: "))  # Handle edge cases
                q2 = int(input("Enter the second target qubit: "))  # Handle edge cases
                self.gate_operations[gate](control, q1, q2)

            else:
                print("Invalid gate. Please choose from the available options.")

    def create_circuit(self, file_name: str):
        with open(file_name, "r") as file:
            for line in file:
                query = line.strip()
                if not query:
                    break
                gate, qubits = self.__parse_string(query)
                self.gate_mappings[gate](*qubits)

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
