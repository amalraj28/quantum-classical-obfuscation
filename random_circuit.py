import numpy as np
from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
from qiskit.qasm2 import dump, load

# Parameters for the random circuit
# Change them accordingly
num_qubits = 4
depth = 3

# Initialize a quantum circuit
qc = QuantumCircuit(num_qubits, num_qubits)

# Define possible gates to apply
single_qubit_gates = ["x", "y", "z", "s", "t", "h"]
two_qubit_gates = ["cx", "cz"]

# Apply random gates to the circuit
for _ in range(depth):
  for qubit in range(num_qubits):
      gate = np.random.choice(single_qubit_gates)
      if gate == "x":
          qc.x(qubit)
      elif gate == "y":
          qc.y(qubit)
      elif gate == "z":
          qc.z(qubit)
      elif gate == "h":
          qc.h(qubit)
      elif gate == "s":
          qc.s(qubit)
      elif gate == "t":
          qc.t(qubit)

      # Apply a random two-qubit gate
      if num_qubits > 1:
          control_qubit = np.random.randint(num_qubits)
          target_qubit = (control_qubit + np.random.randint(1, num_qubits)) % num_qubits
          two_qubit_gate = np.random.choice(two_qubit_gates)
          if two_qubit_gate == "cx":
              qc.cx(control_qubit, target_qubit)
          elif two_qubit_gate == "cz":
              qc.cz(control_qubit, target_qubit)

# Add measurement operations
# qc.measure(range(num_qubits), range(num_qubits))
print(qc.depth())

# Output the circuit as QASM

with open('output.qasm', 'w') as file:
    qasm_output = dump(qc, file)
# print(qasm_output)
print(qc.draw(output="text"))
# plt.show()
