from itertools import permutations
def possible_permutations(ll):
    for permutation in permutations(ll):
        yield list(permutation)


[print(n) for n in possible_permutations([1, 2, 3])]