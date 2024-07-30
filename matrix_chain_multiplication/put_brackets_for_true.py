def is_symbol(char : str) -> bool:
    return char in [ "|", "^", "&"]

def compute( first_val, second_val, operator ):
    operator_and_operation = { "|" : lambda x, y : x or y,
                               "^" : lambda x, y : x ^ y,
                               "&" : lambda x, y : x and y }
    
    return operator_and_operation[ operator ](first_val, second_val)

def solve(string: str, i = 0, j = None):
    if j is None:
        j = len(string)
    
    if i == j:
        return string[i - 1]
    
    elif i + 1 == j:
        return string[i]
    
    num_of_ways = 0

    for k in range(i, j):
        if string[k] in ["|", "^", "&"]:
            
            computed_exp = compute(solve(string, i, k), solve(string, k + 1, j), string[k])
            if computed_exp == "1":
                num_of_ways += 1
        
    return num_of_ways

def solve_dp(string: str):
    dp = [[0 for _ in string] for _ in string]

    def initialize_dp():
        for i in range(len(dp)):
            for j in range(len(dp)):

                if i == j and not is_symbol(string[i-1]):
                    dp[i][j] = string[i-1]

                if i + 1 == j and not is_symbol(string[i]):
                    dp[i][j] = string[i]

                

string = "1&0|1&1"
print(solve(string))

