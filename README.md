# Quantum Playground

A beginner-friendly Qiskit project that builds up from a single qubit to a quantum random number generator. All scripts run on the local Aer simulator, so no quantum hardware or account is needed.

## What's inside

| Script | What it shows |
|--------|---------------|
| `src/01_coin_flip.py` | Superposition: a Hadamard gate makes a qubit 50/50 between 0 and 1 |
| `src/02_bell_state.py` | Entanglement: two qubits that always give matching results (`00` or `11`) |
| `src/03_random_number.py` | A quantum random number generator built from 8 qubits in superposition |

## Bell state circuit

![Bell circuit](bell_circuit.png)

H puts qubit 0 in superposition, and the CNOT entangles qubit 1 with it. Measuring gives `00` or `11` about 50% of the time each, and never `01` or `10`.

## Setup

```bash
git clone https://github.com/adarshpatil1/quantum-playground.git
cd quantum-playground
python -m venv venv
venv\Scripts\activate        # Mac/Linux: source venv/bin/activate
pip install -r requirements.txt
```

## Run

```bash
python src/01_coin_flip.py
python src/02_bell_state.py
python src/03_random_number.py
```

## Built with

- [Qiskit](https://www.ibm.com/quantum/qiskit)
- Qiskit Aer (simulator)
- Matplotlib

## Ideas for next steps

- Quantum teleportation
- Grover's search algorithm
- Running the Bell circuit on real IBM quantum hardware and comparing the noisy results