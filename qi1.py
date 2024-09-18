from qiskit import *   #import q-computing library
circuit = QuantumCircuit(1, 1) #define input array to be(1, 1)
circuit.h(0)#use Hadamard gate method to compress the input array
circuit.measure([0], [0])#meaure the probabilities of compressed(kitsed) array to be (0,0)