from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

bell = QuantumCircuit(2, 2)
bell.h(0)               # superposition on qubit 0
bell.cx(0, 1)           # CNOT: entangle qubit 1 with qubit 0
bell.measure([0, 1], [0, 1])

sim = AerSimulator()
result = sim.run(transpile(bell, sim), shots=1000).result()
counts = result.get_counts()
print(counts)           # only '00' and '11' should appear

plot_histogram(counts)
bell.draw("mpl", filename = "Bell Circuit.png")
plt.show()