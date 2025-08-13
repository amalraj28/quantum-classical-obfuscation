# Quantum encryption, Classical decryption of quantum circuits

This is the codebase of our technique aimed at obfuscating quantum circuits. 

# Background

The technique is aimed at protecting quantum circuits from adversaries. Scheme works by appending random gates to the end of original circuits. These gates could be any gate except Hadamard gate and/or its controlled versions. This would totally corrupt the functionality of the circuit. The added gates are indexed to form a key, which is then used to restore the functionality of the circuit.

# Implementation details

The code is written in Python, utilizing [Qiskit]() framework for coding up the quantum circuit. The technique was developed in Python 3.11.3, with Qiskit 1.3.2.

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
   git clone https://github.com/amalraj28/quantum-classical-obfuscation.git
   ```
7. Install the required packages using the command:
   ```
   pip install -r requirements.txt
   ```
8. Run `main.py` file to start executing the program.

