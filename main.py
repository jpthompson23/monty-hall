import random
from collections import Counter

door_indices = [0, 1, 2]


def simulate(do_switch_choice):
    doors = [False]*3
    prize_door = random.choice(door_indices)
    doors[prize_door] = True
    my_choice = random.choice(door_indices)
    if do_switch_choice:
        reveal_set = set(door_indices)
        reveal_set.discard(prize_door)
        reveal_set.discard(my_choice)
        reveal = reveal_set.pop()
        choice_set = set(door_indices)
        choice_set.discard(reveal)
        choice_set.discard(my_choice)
        my_choice = choice_set.pop()
    return doors[my_choice]


def run_simulations(n, do_switch_choice=False):
    results = []
    for i in range(n):
        res = simulate(do_switch_choice)
        results.append(res)
    counts = Counter(results)
    print("correct: ", counts[True])
    print("incorrect: ", counts[False])


if __name__ == "__main__":
    N = 100000
    print("Without switching:")
    run_simulations(N)
    print("With switching:")
    run_simulations(N, do_switch_choice=True)
