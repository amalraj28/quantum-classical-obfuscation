import matplotlib
import matplotlib.pyplot as plt
from copy import deepcopy
from collections import defaultdict
import numpy as np
import ast
from qiskit.circuit.library import EfficientSU2
from qiskit.quantum_info import SparsePauliOp
from scipy.optimize import minimize
from qiskit import QuantumCircuit, transpile, ClassicalRegister, QuantumRegister, AncillaRegister
from qiskit_aer import AerSimulator
from qiskit_ibm_runtime import EstimatorV2, SamplerV2
from itertools import chain
from qiskit.visualization import plot_histogram, circuit_drawer
import matplotlib.pyplot as plt
from dequeue import Deque
from helper import *
import random
from codes.Grover import Grover
from codes.BernsteinVazirani import BernsteinVazirani as BV
from codes.QAOA import QAOA
from codes.HHL import HHL
from codes.Shor import Shor
import os
from fractions import Fraction
import re