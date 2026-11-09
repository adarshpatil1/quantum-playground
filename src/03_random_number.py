from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

sim = AerSimulator()

def quantum_random(n_bits=8):
    qc = QuantumCircuit(n_bits, n_bits)
    qc.h(range(n_bits))                    # every qubit in 50/50 superposition
    qc.measure(range(n_bits), range(n_bits))
    result = sim.run(transpile(qc, sim), shots=1).result()
    bits = list(result.get_counts().keys())[0]
    return int(bits, 2)

if __name__ == "__main__":
    numbers = [quantum_random(8) for _ in range(10)]
    print("Ten quantum random numbers (0-255):", numbers)