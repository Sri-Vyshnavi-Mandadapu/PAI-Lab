states = ["Low", "Medium", "High"]
actions = ["Short", "Medium", "Long"]
gamma = 0.9
reward = {
    "Low": 10,
    "Medium": 5,
    "High": -10
}
V = {s: 0 for s in states}
for _ in range(20):
    new_V = {}
    for s in states:
        new_V[s] = max(
            reward[s] + gamma * V[s]
            for a in actions
        )
    V = new_V
print("Optimal State Values for Traffic Control:", V)
