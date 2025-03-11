from imports import *


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
            0: "X",
            1: "CX",
            2: "SWAP",
            3: "CCX",
            4: "CSWAP",
            5: "S",
            6: "I",
        }

        self.qubit_count = {
            "X": 1,
            "CX": 2,
            "SWAP": 2,
            "CCX": 3,
            "CSWAP": 3,
            "S": 1,
            "I": 1,
        }

    @classmethod
    def from_qasm2(cls, file_name: str):
        qc = read_qasm2(file_name)
        return cls(qc)

    @classmethod
    def from_qasm3(cls, file_name: str):
        qc = read_qasm3(file_name)
        return cls(qc)

    def to_qasm2(self, file_name: str):
        write_qasm2(self.qc, file_name)

    def to_qasm3(self, file_name: str):
        write_qasm3(self.qc, file_name)

    def encrypt(self, key_size: int, effective_qubits: int = -1) -> str:
        rem = key_size
        key: list[list[int]] = []
        if effective_qubits == -1:
            effective_qubits = self.qc.num_qubits

        while rem > 0:
            idx = random.randint(0, len(list(self.gate_index.keys())) - 1)
            gate = self.gate_index[idx]
            contr = self.qubit_count[gate] + 1

            if (rem - contr == 0 or rem - contr > 1) and contr - 1 <= effective_qubits:
                encryptor: list[int] = []
                encryptor.append(idx)

                qubits = random.sample(range(effective_qubits), contr - 1)
                self.gate_mappings[gate](*qubits)
                encryptor.extend(qubits)
                key.append(encryptor)
                rem -= contr

        flattened_list = list(map(lambda x: str(x), chain.from_iterable(key)))

        return "".join(flattened_list)

    def decrypt(self, key: str, incorrect_measure: str, effective_qubits: int = -1):
        deque = Deque()
        measurement = [int(x) for x in incorrect_measure]

        n = effective_qubits

        if n == -1:
            n = self.qc.num_qubits

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

            else:
                continue

        return "".join(list(map(str, measurement)))

    def measure(
        self, add_bits: bool = False, measure_all: bool = True, num_qubits: int = 0
    ):
        if measure_all:
            self.qc.measure_all(add_bits=add_bits)
        else:
            self.qc.measure(range(num_qubits), range(num_qubits))

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


def execute_grover(solution_sets: list[list[str]] | None = None, key_size: int = 20):
    def generate_grover_circuits(solutions: list[list[str]], folder_path: str):
        grover = Grover()
        for idx in range(len(solutions)):
            qc = grover.create_grover_ciruit(solutions[idx])
            file_name = generate_unique_string()
            write_qasm3(qc, f"{folder_path}/{file_name}.qasm")
            with open(f"{folder_path}/{file_name}.qasm", "a") as file:
                file.write(f"\n\n//Solutions = {solutions[idx]}")

        print("Generated qasm files for the Grover circuits of provided solution sets.")

    qasm_folder_path = "qasm_files1/grover"

    if solution_sets is not None:
        if not os.path.exists(qasm_folder_path):
            os.makedirs(qasm_folder_path)
        generate_grover_circuits(solution_sets, qasm_folder_path)

    for file in os.listdir(qasm_folder_path):
        if os.path.isfile(os.path.join(qasm_folder_path, file)):
            qc = QCircuit.from_qasm3(os.path.join(qasm_folder_path, file))
            qc_copy = deepcopy(qc)

            qc_copy.measure(add_bits=True)
            qc_copy.draw(filename="pics/grover/original_circuit.png", output="mpl")
            _, res_orig = qc_copy.compile_and_run()
            plot_histogram(res_orig, title="Original State (before encryption)")
            plt.savefig("pics/grover/original_result.png")
            # plt.show()

            key: str = qc.encrypt(key_size)
            qc.measure(add_bits=True)
            qc.draw(filename="pics/grover/encrypted_circuit.png", output="mpl")
            _, res = qc.compile_and_run()
            print(f"Incorrect result = {res}")

            plot_histogram(res, title="Incorrect matching state (after encryption)")
            plt.savefig("pics/grover/encrypted_result.png")
            # # plt.show()

            corrected_res = {}

            for string, shots in res.items():
                decrypted_measure = qc.decrypt(key, string)
                corrected_res[decrypted_measure] = shots

            plot_histogram(corrected_res, title="Actual measurement (decrypted)")
            plt.savefig("pics/grover/decrypted_result.png")
            # # plt.show()


def execute_bv(solution_sets: list[list[str]] | None = None):
    def generate_bv_circuits(solutions: list[list], folder_path: str):
        factor: str = ""
        bias: int = 0

        for item in solutions:
            factor = item[0]
            if len(item) == 2:
                bias = item[1]  # type: ignore

            bv = BV(factor, bias)
            for idx in range(len(solutions)):
                qc = bv.create_circuit(add_measurement=False)
                file_name = generate_unique_string()
                write_qasm2(qc, f"{folder_path}/{file_name}.qasm")
                with open(f"{folder_path}/{file_name}.qasm", "a") as file:
                    file.write(f"\n\n//Solutions = {solutions[idx]}")

        print(
            "Generated qasm files for the Bernstein Vazirani circuits of provided solution sets."
        )

    qasm_folder_path = "qasm_files1/bv"

    if solution_sets is not None:
        if not os.path.exists(qasm_folder_path):
            os.makedirs(qasm_folder_path)
        generate_bv_circuits(solution_sets, qasm_folder_path)

    for file in os.listdir(qasm_folder_path):
        if os.path.isfile(os.path.join(qasm_folder_path, file)):
            qc = QCircuit.from_qasm2(os.path.join(qasm_folder_path, file))
            qc_copy = deepcopy(qc)

            qc_copy.measure(num_qubits=qc.qc.num_qubits - 1, measure_all=False)
            qc_copy.draw(filename="pics/bv/original_circuit.png")
            _, res_orig = qc_copy.compile_and_run(shots=20)
            plot_histogram(res_orig, title="Actual marked state (without encryption)")
            plt.savefig("pics/bv/original_result.png")
            # plt.show()

            qc.qc.barrier()
            key: str = qc.encrypt(20, effective_qubits=qc.qc.num_qubits - 1)
            qc.qc.barrier()
            qc.measure(num_qubits=qc.qc.num_qubits - 1, measure_all=False)
            qc.draw(filename="pics/bv/encrypted_circuit.png", output="mpl")
            _, res = qc.compile_and_run(shots=20)
            plot_histogram(res, title="Marked State after encryption")
            plt.savefig("pics/bv/encrypted_result.png")
            # plt.show()
            corrected_res = {}

            for string, shots in res.items():
                decrypted_measure = qc.decrypt(
                    key, string, effective_qubits=qc.qc.num_qubits - 1
                )
                corrected_res[decrypted_measure] = shots

            plot_histogram(corrected_res, title="Marked state after decryption")
            plt.savefig("pics/bv/decrypted_result.png")
            # plt.show()


def execute_qaoa(
    adjacency_list: list[tuple[int, int, int | float]] | None,
    num_qubits: int,
    reps: int,
):
    def generate_qaoa_circuit(
        adjacency_list: list[tuple[int, int, int | float]], folder_path: str
    ):
        qaoa = QAOA(num_qubits, adjacency_list)
        circuit = qaoa.create_circuit(reps=reps, measure_all=False)
        backend = AerSimulator()
        transpiled, result, objective_vals = qaoa.compile_and_run_circuit(
            circuit, backend, reps=reps, cost_hamiltonian=qaoa.cost_hamiltonian
        )
        file_name = f"{folder_path}/{generate_unique_string()}.qasm"
        write_qasm3(transpiled, file_name)
        with open(file_name, "a") as file:
            file.write(f"\n\n//Adjacency list = {adjacency_list}")

        print("Generated qasm files for the QAOA circuit of provided solution sets.")

    qasm_folder_path = "qasm_files1/qaoa"

    if adjacency_list is not None:
        if not os.path.exists(qasm_folder_path):
            os.makedirs(qasm_folder_path)
        generate_qaoa_circuit(adjacency_list, qasm_folder_path)

    for file in os.listdir(qasm_folder_path):
        if os.path.isfile(os.path.join(qasm_folder_path, file)):
            qc = QCircuit.from_qasm3(os.path.join(qasm_folder_path, file))
            qc_copy = deepcopy(qc)

            qc.measure(add_bits=True)
            qc.draw(filename="pics/qaoa/original_circuit.png", output="mpl")
            _, res = qc.compile_and_run(shots=1024)
            plot_histogram(res, title="Original Result (without encryption)")
            plt.savefig("pics/qaoa/original_result.png")
            # plt.show()

            qc_copy.qc.barrier()
            key: str = qc_copy.encrypt(20)
            qc_copy.qc.barrier()
            # print("Completed a file")
            qc_copy.measure(add_bits=True)
            qc_copy.draw(filename="pics/qaoa/encrypted_circuit.png", output="mpl")
            _, encrypted_res = qc_copy.compile_and_run(shots=1024)
            plot_histogram(encrypted_res, title="Encrypted Result")
            plt.savefig("pics/qaoa/encrypted_result.png")
            # plt.show()

            corrected_res = {}

            for string, shots in res.items():
                decrypted_measure = qc.decrypt(key, string)
                corrected_res[decrypted_measure] = shots

            plot_histogram(res, title="Decrypted Result")
            plt.savefig("pics/qaoa/decrypted_result.png")
            # plt.show()


def execute_vqe():
    hamiltonian = SparsePauliOp.from_list(
        [("YZ", 0.3980), ("ZI", -0.3980), ("ZZ", -0.0113), ("XX", 0.1810)]
    )
    ansatz = EfficientSU2(hamiltonian.num_qubits)
    backend = AerSimulator()
    estimator = EstimatorV2(mode=backend)
    sampler = SamplerV2(mode=backend)
    vqe = VQE(ansatz, hamiltonian, estimator, sampler)
    vqe.draw(ansatz, title="Ansatz before compiling")
    ansatz_copy = vqe.get_uncompiled_ansatz()
    vqe.compile_ansatz(backend)


def execute_hhl(initial_state: list[float] | None = None, clock_reg: int = 2, shots: int = 1024, generate_circuit: bool = False):
    def generate_hhl_circuit(folder_path: str, initial_state: list[float] | None=None):
        # Create HHL instance
        qc = HHL(clock_reg=clock_reg)
        
        # State preparation
        if initial_state is not None:
            qc.qc.initialize(initial_state, qc.input_reg[0])
        else:
            qc.qc.x(qc.input_reg)  # Default to |1> as in your original
        
        # Build the full circuit
        qc.qc.h(qc.clock)
        qc.hhl()
        qc.qc.h(qc.clock)
        # hhl.qc.measure(hhl.input_reg[0], hhl.measurement[1])
        
        # Transpile and save as QASM3
        # backend = AerSimulator()
        # transpiled = transpile(hhl.qc, backend=backend)
        file_name = f"{folder_path}/{generate_unique_string()}.qasm"
        write_qasm3(qc.qc, file_name)  # Qiskit’s QASM3 exporter
        with open(file_name, "a") as f:
            f.write(f"\n\n// Initial state = {initial_state if initial_state else '[0, 1]'}")
        
        print("Generated QASM file for the HHL circuit.")
    
        
    # Define folder path for QASM files
    qasm_folder_path = "qasm_files/hhl"
    # generate_hhl_circuit(folder_path=qasm_folder_path)
    # exit()
    
    if generate_circuit:
        if not os.path.exists(qasm_folder_path):
            os.makedirs(qasm_folder_path)
    
        generate_hhl_circuit(qasm_folder_path)
    
    # Load and process each QASM file (mimicking execute_qaoa)
    for file in os.listdir(qasm_folder_path):
        if os.path.isfile(os.path.join(qasm_folder_path, file)):
            # Load QASM into a new circuit
            qc = QCircuit.from_qasm3(os.path.join(qasm_folder_path, file))
            qc_copy = deepcopy(qc)

            # Original circuit execution
            qc.measure(measure_all=True, add_bits=True)
            qc.draw(output="mpl", filename="pics/hhl/original_circuit.png")
            _, res = qc.compile_and_run(shots=10000)
            print(res)
            plot_histogram(res, title="Original Result (without encryption)")
            plt.savefig("pics/hhl/original_result.png")
            plt.close()

            # Encrypted circuit (stubbed, as HHL class lacks encrypt/decrypt)
            qc_copy.qc.barrier()
            key = qc_copy.encrypt(key_size=20)
            qc_copy.measure(measure_all=True, add_bits=True)
            # If you had an encrypt method, it would go here
            # key = qc_copy.encrypt(20)  # Example, not implemented
            qc_copy.draw(output="mpl", filename="pics/hhl/encrypted_circuit.png")
            _, encrypted_res = qc_copy.compile_and_run(shots=10000)
            print(encrypted_res)
            plot_histogram(encrypted_res, title="Encrypted Result")
            plt.savefig("pics/hhl/encrypted_result.png")
            plt.close()

            # Decrypted result (stubbed, as no decryption is implemented)
            # corrected_res = encrypted_res  # Placeholder; no decryption logic
            # plot_histogram(corrected_res, title="Decrypted Result (no decryption applied)")
            # plt.savefig("pics/hhl/decrypted_result.png")
            # plt.close()
            corrected_res = {}

            for string, shots in encrypted_res.items():
                decrypted_measure = qc.decrypt(key, string)
                corrected_res[decrypted_measure] = shots

            plot_histogram(corrected_res, title="Decrypted Result")
            plt.savefig("pics/hhl/decrypted_result.png")
            # plt.show()


if __name__ == "__main__":
    # execute_grover([['1101']])
    # execute_bv([['10101010']])
    # execute_qaoa(
    #     [(0, 1, 1.0), (0, 2, 1.0), (0, 4, 1.0), (1, 2, 1.0), (2, 3, 1.0), (3, 4, 1.0)],
    #     num_qubits=5,
    #     reps=2,
    # )
    execute_hhl(generate_circuit=True)