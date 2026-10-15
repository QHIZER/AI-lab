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


output

8 QUEENS - SIMULATED ANNEALING
Step 0: State=[1, 1, 1, 1, 1, 1, 1, 1], h=28, T=100.00
Move: Column 2 -> Row 5
Step 1: State=[1, 5, 1, 1, 1, 1, 1, 1], h=22, T=95.00
Move: Column 3 -> Row 8
Step 2: State=[1, 5, 8, 1, 1, 1, 1, 1], h=16, T=90.25
Move: Column 4 -> Row 6
Step 3: State=[1, 5, 8, 6, 1, 1, 1, 1], h=11, T=85.74
Move: Column 5 -> Row 3
Step 4: State=[1, 5, 8, 6, 3, 1, 1, 1], h=8, T=81.45
Move: Column 6 -> Row 7
Step 5: State=[1, 5, 8, 6, 3, 7, 1, 1], h=4, T=77.38
Move: Column 7 -> Row 2
Step 6: State=[1, 5, 8, 6, 3, 7, 2, 1], h=2, T=73.51
Move: Column 8 -> Row 4
Final State=[1, 5, 8, 6, 3, 7, 2, 4], h=0
Solution found!

