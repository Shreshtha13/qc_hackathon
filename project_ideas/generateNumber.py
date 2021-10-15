from qiskit import *
from qiskit import IBMQ
import math
import matplotlib.pyplot as plt
noOfDigits = 2
circuit = QuantumCircuit(noOfDigits,noOfDigits)
circuit.h(range(noOfDigits))
circuit.measure(range(noOfDigits), range(noOfDigits))
circuit.draw(output='mpl')
# plt.show()
# print(circuit)

simulator = Aer.get_backend('qasm_simulator')
result = execute(circuit,backend=simulator, shots=1).result()
counts = result.get_counts()
random_number = 0
for i,j in counts.items():
    random_number = i

# print(random_number)
