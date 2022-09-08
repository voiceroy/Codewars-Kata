def permutations(s: str) -> list:
    from itertools import permutations as permute

    permuted = list({"".join(x) for x in permute(s)})
    return permuted
