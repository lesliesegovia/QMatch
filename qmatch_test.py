from qiskit import QuantumCircuit, Aer, execute

# ask the player a question
# the idea is to think like a classical computer
player_guess = input("Do you think the two cards will match? (y/n): ").lower()

# setting up the 2 quibit game
qc = QuantumCircuit(2, 2)
qc.h(0)
qc.h(1)

qc.measure(0, 0)
qc.measure(1, 1)

# simulating a round
backend = Aer.get_backend('qasm_simulator')
result = execute(qc, backend, shots=1).result()
counts = result.get_counts()

# there will only be one result
outcome = list(counts.keys())[0]
card2, card1 = outcome[0], outcome[1]

print("\nYou flipped the first card and saw:", card1)
print("You flipped the second card and saw:", card2)

if card1 == card2:
    print("🎉 They matched!")
    actual_match = 'y'
else:
    print("❌ Not a match.")
    actual_match = 'n'

# show player's result
if player_guess == actual_match:
    print("✅ You guessed right!")
else:
    print("❌ Your guess was wrong... but quantum is tricky!")