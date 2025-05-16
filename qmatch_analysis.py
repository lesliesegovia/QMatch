from qiskit import QuantumCircuit, Aer, execute
import matplotlib.pyplot as plt

# Ask about entanglement
entangle_choice = input("Run with entanglement? (y/n): ").lower()

qc = QuantumCircuit(2, 2)
qc.h(0)

if entangle_choice == 'y':
    qc.cx(0, 1)
else:
    qc.h(1)

qc.measure(0, 0)
qc.measure(1, 1)

# run 1000 shots
backend = Aer.get_backend('qasm_simulator')
result = execute(qc, backend, shots=1000).result()
counts = result.get_counts()

# matches
matches = counts.get('00', 0) + counts.get('11', 0)
non_matches = counts.get('01', 0) + counts.get('10', 0)

# results
print("Match Stats (1000 rounds):")
print(f"Matches: {matches}")
print(f"Non-Matches: {non_matches}")

labels = ['Matches', 'Non-Matches']
values = [matches, non_matches]

plt.bar(labels, values, color=['mediumseagreen', 'tomato'])
plt.title(f"Quantum Match Results (Entangled = {entangle_choice.upper()})")
plt.ylabel('Count')
plt.show()
