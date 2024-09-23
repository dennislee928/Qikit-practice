import sys
print("Python executable:", sys.executable)
print("sys.path:", sys.path)

from qiskit import Aer, execute  # 新增 execute 的匯入
from qiskit import QuantumCircuit

from setuptools import setup, find_packages  # type: ignore #import q-computing library
circuit = QuantumCircuit(1, 1) #define input array to be(1, 1)
circuit.h(0)#use Hadamard gate method to compress the input array
circuit.measure([0], [0])#meaure the probabilities of compressed(kitsed) array to be (0,0)



simulator = Aer.get_backend('qasm_simulator')  # 修改 per 為 Aer
result = execute(circuit, simulator).result()




counts = result.get_counts(circuit)
print(counts) 