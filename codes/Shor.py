# Code taken from the below website and modified to fit our framework
# https://github.com/Qiskit/textbook/blob/main/notebooks/ch-algorithms/shor.ipynb

from qiskit import QuantumCircuit, QuantumRegister
import numpy as np
import copy


class Shor:
    def __init__(self, N: int, a: int):
        """Initialize Shor's algorithm with number to factor and base."""
        self.N = N
        self.a = a
        self.n_count = int(np.ceil(np.log2(self.N)))
        self.n_work = int(np.ceil(np.log2(self.N)))
        
        self.qreg_count = QuantumRegister(self.n_count, "count")
        self.qreg_work = QuantumRegister(self.n_work, "work")
        self.base_circuit = QuantumCircuit(self.qreg_count, self.qreg_work)
        
        for q in range(self.n_count):
            self.base_circuit.h(q)
        self.base_circuit.x(self.n_count)

    def __is_valid_input(self) -> bool:
        """Validate inputs for Shor's algorithm."""
        if self.N <= 1 or self.N % 2 == 0:
            return False
        if self.a <= 1 or self.a >= self.N:
            return False
        if np.gcd(self.a, self.N) != 1:
            return False
        return True

    def __c_amod15(self, a: int, power: int) -> QuantumCircuit:
        """Controlled multiplication by a mod 15, decomposed."""
        if a not in [2, 4, 7, 8, 11, 13]:
            raise ValueError("'a' must be coprime to 15")

        U = QuantumCircuit(self.n_work)
        for _ in range(power):
            if a in [2, 13]:
                U.swap(0, 1)
                U.swap(1, 2)
                U.swap(2, 3)
            if a in [7, 8]:
                U.swap(2, 3)
                U.swap(1, 2)
                U.swap(0, 1)
            if a in [4, 11]:
                U.swap(1, 3)
                U.swap(0, 2)
            if a in [7, 11, 13]:
                for q in range(4):
                    U.x(q)
        return U

    def __qft_dagger(self, n: int) -> QuantumCircuit:
        """n-qubit inverse Quantum Fourier Transform, decomposed."""
        qc = QuantumCircuit(n)
        for qubit in range(n // 2):
            qc.swap(qubit, n - qubit - 1)
        for j in range(n):
            for m in range(j):
                qc.cp(-np.pi / float(2 ** (j - m)), m, j)
            qc.h(j)
        return qc

    def create_shor_circuit(self) -> QuantumCircuit:
        """Generate quantum circuit for Shor's algorithm, fully decomposed."""
        print(f"Factoring N = {self.N} with a = {self.a}")
        if not self.__is_valid_input():
            raise ValueError("Invalid input: N must be odd, > 1, and a must be coprime to N, 1 < a < N")

        qc = copy.deepcopy(self.base_circuit)
        for q in range(self.n_count):
            controlled_U = self.__c_amod15(self.a, 2**q)
            qc.compose(controlled_U.control(), [q] + [self.n_count + i for i in range(self.n_work)], inplace=True)
        
        qc.compose(self.__qft_dagger(self.n_count), range(self.n_count), inplace=True)
        return qc
