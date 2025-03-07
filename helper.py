from qiskit.qasm2 import dump as q2_dump, load as q2_load
from qiskit.qasm3 import dump as q3_dump, load as q3_load
from qiskit import QuantumCircuit
from uuid import uuid4

class Input:
    @staticmethod
    def integer(query: str) -> int:
        while True:
            try:
                n = int(input(query))
            except ValueError:
                print("Invalid input! Try again")
            else:
                break

        return n


def read_qasm2(file_name: str) -> QuantumCircuit:
    file_name = file_name.strip()
    if not file_name.lower().endswith(".qasm"):
        raise ValueError(f"{file_name} is not a valid QASM2 file.")

    return q2_load(file_name)

def read_qasm3(file_name: str):
    file_name = file_name.strip()
    if not file_name.lower().endswith(".qasm"):
        raise ValueError(f"{file_name} is not a valid QASM3 file.")

    return q3_load(file_name)

def write_qasm3(qc: QuantumCircuit, file_name: str):
    if not file_name.lower().endswith('.qasm'):
        raise ValueError(f"{file_name} is not a valid QASM3 file name.")
    
    with open(file_name, 'w') as file:
        q3_dump(qc, file)

def write_qasm2(qc: QuantumCircuit, file_name: str):
    if not file_name.lower().endswith('.qasm'):
        raise ValueError(f"{file_name} is not a valid QASM2 file name.")
    
    with open(file_name, 'w') as file:
        q2_dump(qc, file)

def generate_unique_string() -> str:
    return str(uuid4()).replace('-', '')