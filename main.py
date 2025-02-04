from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt
from stack import Stack

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


n = int(input("Enter the number of qubits: "))  # Handle edge cases
qc = create_circuit(n)
valid_gates = ["CX", "CCX", "SWAP", "CSWAP"]
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

stack = Stack()

while True:
    prompt = input(
        "Enter the gates and qubit to be added at the end of circuit, separated by space (leave blank for exiting): "
    )
    if len(prompt) == 0:
        break

    gate, qubits = parse_string(prompt)
    qc = add_classical_gate(qc, gate, qubits)
    stack.push((gate, qubits))

qc.measure_all()

transpiled, results = compile_and_run(qc)

measurements = results.keys()

