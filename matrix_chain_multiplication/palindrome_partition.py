import sys

def is_palindrome(string: str) -> bool:
    return string == string[::-1]

def solve(string: str, i: int = 0, j = None) -> int:
    if j is None:
        j = len(string)

    if i >= j:
        return 0
    
    if is_palindrome(string[i:j]):
        return 0
    
    min_num = sys.maxsize

    for k in range(i + 1, j):
        num = solve(string, i, k) + solve(string, k, j) + 1
        min_num = min(min_num, num)
    
    return min_num

def solve_dp(string : str):
    dp = [[0 for _ in string] for _ in string]

    def fill_dp():

        for i in range(len(dp)):
            for j in range(len(dp)):
                
                if i + 1 < j and not is_palindrome(string[i:j+1]):
                    dp[i][j] = min([dp[i][k] + dp[k][j] + 1 for k in range(i+1,j)])

    for _ in range(len(string)):
        fill_dp()
        print(dp)

    return dp[0][-1]

print(solve_dp("ITI"))