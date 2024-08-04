from functools import lru_cache

@lru_cache(maxsize=1000)
def solve(string1 : str, string2 : str):

    if string1 == string2:
        return True

    if len(string1) != len(string2):
        return False
    
    if sorted(string1) != sorted(string2):
        return False
    
    for k in range(1, len(string1)):
        with_swapping = solve(string1[ : k], string2[-k : ]) and solve(string1[k : ], string2[ : -k])
        without_swapping = solve(string1[ : k], string2[ : k]) and solve(string1[k : ], string2[k : ])

        if with_swapping or without_swapping:
            return True

    return False

def solve2(string1: str, string2: str) -> bool:
    # If strings are identical, return True
    if string1 == string2:
        return True
    
    # If lengths are different, return False
    if len(string1) != len(string2):
        return False
    
    # If the sorted characters of both strings are different, return False
    if sorted(string1) != sorted(string2):
        return False
    
    n = len(string1)
    
    # Check all possible ways to split the strings
    for k in range(1, n):
        # Check if the current split is valid with or without swapping
        with_swapping = solve(string1[:k], string2[k:]) and solve(string1[k:], string2[:k])
        without_swapping = solve(string1[:k], string2[:k]) and solve(string1[k:], string2[k:])
        
        if with_swapping or without_swapping:
            return True

    return False

print(solve("great", "eatgr"))