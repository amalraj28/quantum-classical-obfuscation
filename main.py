from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

def create_circuit(n: int):
    pass
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
            q1 = int(input("Enter the first qubit: ")) # Handle edge cases
            q2 = int(input("Enter the second qubit: ")) # Handle edge cases
            gates[gate](q1, q2)

        else:
            print("Invalid gate. Please choose from the available options.")
        
        qc.measure_all()

    return qc

def compile_and_run(circuit: QuantumCircuit):
    simulator = AerSimulator()
    transpiled = transpile(circuit, simulator)
    result = simulator.run(transpiled, shots=1024).result()
    print(result.get_counts())

    # return transpiled, result.get_counts()
    return [], []

# n = int(input("Enter the number of qubits: "))  # Handle edge cases
# qc = create_circuit(n)

qc = QuantumCircuit(3)
qc.x(1)
qc.h(0)
qc.cx(1, 2)
qc.measure_all()

# transpiled, result = compile_and_run(qc)

qc.draw(output='mpl')