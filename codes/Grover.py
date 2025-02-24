# Some of the codes are taken from IBM
# Link: https://learning.quantum.ibm.com/tutorial/grovers-algorithm

from qiskit import QuantumCircuit
from qiskit.circuit.library import MCMT, ZGate, GroverOperator
import math


class Grover:
    def __is_valid_solution(self, solutions: list[str]) -> bool:
        if len(solutions) == 0:
            return False

        length = len(solutions[0])

        for soln in solutions[1:]:
            if len(soln) != length:
                return False

        return True

    # Oracle function taken as is from IBM Learning
    def __grover_oracle(self, marked_states) -> QuantumCircuit:
        """Build a Grover oracle for multiple marked states

        Here we assume all input marked states have the same number of bits

        Parameters:
            marked_states (str or list): Marked states of oracle

        Returns:
            QuantumCircuit: Quantum circuit representing Grover oracle
        """
        if not isinstance(marked_states, list):
            marked_states = [marked_states]
        # Compute the number of qubits in circuit
        num_qubits = len(marked_states[0])

        qc = QuantumCircuit(num_qubits)
        # Mark each target state in the input list
        for target in marked_states:
            # Flip target bit-string to match Qiskit bit-ordering
            rev_target = target[::-1]
            # Find the indices of all the '0' elements in bit-string
            zero_inds = [
                ind for ind in range(num_qubits) if rev_target.startswith("0", ind)
            ]
            # Add a multi-controlled Z-gate with pre- and post-applied X-gates (open-controls)
            # where the target bit-string has a '0' entry
            qc.x(zero_inds)
            qc.compose(MCMT(ZGate(), num_qubits - 1, 1), inplace=True)
            qc.x(zero_inds)
        return qc

    def create_grover_ciruit(self, solutions: list[str]) -> QuantumCircuit:
        """Function to generate quantum circuit implementing Grover's algorithm.

        Args:
            solutions (list[str]): The solution set. Must be a list of binary strings.

        Raises:
            Exception: if solution set is empty
            Exception: if solution set has strings with unequal length

        Returns:
            QuantumCircuit: Final quantum circuit after appending oracle and Grover's operator.
            Measurement gates are not added to the circuit.
        """
        if len(solutions) == 0:
            raise Exception(
                "Current implementation is only for the case of known solutions!"
            )

        if not self.__is_valid_solution(solutions):
            raise Exception("All solutions must have same number of bits!")

        oracle: QuantumCircuit = self.__grover_oracle(solutions)
        num_qubits: int = len(solutions[0])
        grover_op = GroverOperator(oracle)
        qc = QuantumCircuit(num_qubits)

        qc.h(range(num_qubits))

        optimal_iter: int = math.floor(
            (math.pi / (4 * math.asin(math.sqrt(len(solutions) / 2**num_qubits))))
        )

        qc.compose(grover_op.power(optimal_iter), inplace=True)

        return qc
