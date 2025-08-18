# Quantum encryption, Classical decryption of quantum circuits

This is the codebase of our technique aimed at obfuscating quantum circuits. 

# Background

The technique is aimed at protecting quantum circuits from adversaries. Scheme works by appending random gates to the end of original circuits. These gates could be any gate except Hadamard gate and/or its controlled versions. This would totally corrupt the functionality of the circuit. The added gates are indexed to form a key, which is then used to restore the functionality of the circuit.

# Implementation details

The code is written in Python, utilizing [Qiskit](https://www.ibm.com/quantum/qiskit) framework for coding up the quantum circuit. The technique was developed in Python 3.11.3, with Qiskit 1.3.2.

# Implementation setup

In order to try out this technique, you can follow the below steps in sequence. 
1. Ensure that Python is installed on your system (preferably 3.11+).
2. Ensure that you have the latest version of pip and virtualenv packages.
3. In your terminal, navigate to the directory where you intend to work on the project
4. Create a virtual environment (let's call it _my_env_), in the project root, using the command `python -m venv my_env` or `python3 -m venv my_env` as per your OS.
5. Activate the virtual environment by running either of the below commands in  your terminal:

   _For windows:_
   ```
   my_env/Scripts/activate
   ```
   _For Linux/MacOS:_
   ```
   source my_env/bin/activate
   ```
6. Clone this repository into the project root by running the following command:
   ```
   git clone https://github.com/vivekianity/quantum-classical-obfuscation.git
   ```
7. Install the required packages using the command:
   ```
   pip install -r requirements.txt
   ```
8. Run `main.py` file to start executing the program.

# Program structure

The codebase has been organized into various folders for easy understanding. In the project root, `main.py` is the entry point to the program. The file consists of the _QCircuit_ class, which can be considered as the wrapper class consisting of all the required methods, which includes reading from and writing to QASM files, encryption of QuantumCircuit objects, generation of encryption keys, decryption using the keys, computing TVD and DFC etc. The class allows quantum circuits to be given as inputs via OPENQASM files (both 2.0 and 3.0), as well as manually specifying the required arguments. 

Each technique to be evaluated is written as a function named _execute\_{technique_name}_, such as `execute_shor`, `execute_grover` and so on. The functions are written on the logic that if the solution set is provided as input (such as solutions to be searched by Grover algorithm, or adjacency list needed for graph generation for QAOA algorithms), the QASM file corresponding to that solution is generated and stored in `qasm_files` folder. If the argument is not provided (meaning its default value of `None` will be used), it is implied that the QASM file needed is already available in `qasm_files` folder under the relevant folder name, without which the program would stop execution.

Each algorithm used to test the encryption scheme is present in the `codes` folder, implemented as classes. Any algorithm that is to be tested could also be placed in the `codes` folder. 

`metrics` folder contains the values of evaluation metrics (TVD and DFC) for the algorithms in `codes` folder.

`pics` folder consists of measurement histograms of unobfuscated, encrypted and decrypted results. 

`qasm_files` store the QASM files for the algorithms.

`dequeue.py` is the custom implementation of doubly-ended queue (deque) data structure. The methods present in `deque` library of `collections` module have been renamed to mirror their functionalities. Deque is needed during decryption.

# Corrections and/or updates to the code

If you feel any missing component or find bug in the code, you can raise an issue under `Issues` tab of GitHub. All code improvements or updates are to be sent as pull requests to this repository.
