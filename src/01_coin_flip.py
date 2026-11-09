from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

qc = QuantumCircuit(1, 1)
qc.h(0)             # Hadamard: 50/50 superposition
qc.measure(0, 0)    # collapse to 0 or 1

sim = AerSimulator()
result = sim.run(transpile(qc, sim), shots=1000).result()
counts = result.get_counts()
print(counts)

plot_histogram(counts)
plt.show()