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
    
    if i == j and i > 0:
        return int(string[i - 1])
    
    elif i + 1 == j:
        return int(string[i])
    
    num_of_ways = 0

    for k in range(i, j):
        if string[k] in ["|", "^", "&"]:
            
            computed_exp = compute(solve(string, i, k), solve(string, k + 1, j), string[k])
            if computed_exp == 1:
                num_of_ways += 1
        
    return num_of_ways

def solve_dp(string: str):
    n = len(string)
    dp = [[0] * n for _ in range(n)]

    def is_digit(c):
        return c.isdigit()

    def is_operator(c):
        return c in ["|", "^", "&"]

    def compute(first_val, second_val, operator):
        operator_and_operation = {
            "|": lambda x, y: x or y,
            "^": lambda x, y: x ^ y,
            "&": lambda x, y: x and y
        }
        return operator_and_operation[operator](first_val, second_val)

    # Initialize DP table
    for i in range(n):
        if is_digit(string[i]):
            dp[i][i] = int(string[i])
    
    # Fill DP table
    for length in range(2, n + 1):  # Length of the substring
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = 0
            for k in range(i, j):
                if is_operator(string[k]):
                    left_val = dp[i][k - 1] if i <= k - 1 else None
                    right_val = dp[k + 1][j] if k + 1 <= j else None
                    if left_val is not None and right_val is not None:
                        result = compute(left_val, right_val, string[k])
                        if result == 1:
                            dp[i][j] += 1

    print(dp)

    return dp[0][n - 1]


string = "1&0|1&1"
print(solve(string))

