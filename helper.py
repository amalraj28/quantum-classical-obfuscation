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
    if not file_name.lower().endswith(".qasm"):
        raise ValueError(f"{file_name} is not a valid QASM3 file name.")

    with open(file_name, "w") as file:
        q3_dump(qc, file)


def write_qasm2(qc: QuantumCircuit, file_name: str):
    if not file_name.lower().endswith(".qasm"):
        raise ValueError(f"{file_name} is not a valid QASM2 file name.")

    with open(file_name, "w") as file:
        q2_dump(qc, file)


def generate_unique_string() -> str:
    return str(uuid4()).replace("-", "")


def calculate_median(values):
    sorted_values = sorted(values)
    n = len(sorted_values)

    if n == 0:
        raise ValueError("List is empty")

    mid = n // 2
    median = (
        (sorted_values[mid - 1] + sorted_values[mid]) / 2
        if n % 2 == 0
        else sorted_values[mid]
    )

    return median


def tvd(original_res, encrypted_res):
    if sum(list(original_res.values())) != sum(list(encrypted_res.values())):
        raise Exception("Size difference for tvd")

    print(f"Count = {sum(list(original_res.values()))}")
    all_keys = set(original_res.keys()).union(encrypted_res.keys())

    return 0.5 * sum(
        abs(original_res.get(k, 0) - encrypted_res.get(k, 0))
        / sum(encrypted_res.values())
        for k in all_keys
    )


def dfc(original_res, encrypted_res):
    correct_output = max(original_res, key=original_res.get)
    correct_count = encrypted_res.get(correct_output, 0)

    incorrect_counts = {k: v for k, v in encrypted_res.items() if k != correct_output}
    max_incorrect_count = max(incorrect_counts.values(), default=0)
    total_shots = sum(encrypted_res.values())
    dfc_score = (correct_count - max_incorrect_count) / total_shots

    return dfc_score
