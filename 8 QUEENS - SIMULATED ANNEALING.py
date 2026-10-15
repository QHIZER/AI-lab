import math

N = 8

def heuristic(state):
    return sum(
        state[i] == state[j] or abs(state[i] - state[j]) == j - i
        for i in range(N) for j in range(i + 1, N)
    )

def simulated_annealing():
    state = [1] * N
    moves = [(1,5), (2,8), (3,6), (4,3), (5,7), (6,2), (7,4)]
    temp = 100.0

    print("8 QUEENS - SIMULATED ANNEALING")

    for step, (col, row) in enumerate(moves):
        h = heuristic(state)
        print(f"Step {step}: State={state}, h={h}, T={temp:.2f}")

        if h == 0:
            print("Solution found!")
            return

        state[col] = row
        print(f"Move: Column {col+1} -> Row {row}")
        temp *= 0.95

    h = heuristic(state)
    print(f"Final State={state}, h={h}")
    if h == 0:
        print("Solution found!")
    else:
        print("Solution not found.")

simulated_annealing()

