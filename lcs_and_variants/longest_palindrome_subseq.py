memo = {}

def longest_palindrome_subseq ( string : str, curr_score = 0):
    if len( string ) <= 1:
        return curr_score + len(string)

    if string[0] == string[-1]:
        remaining_string = string[ 1 : len(string) - 1 ]
        score = memo[remaining_string] if remaining_string in memo else longest_palindrome_subseq ( remaining_string , curr_score + 2 )
        return score

    else:
        str_without_first_char = string [ 1:]
        str_without_last_char = string [ :-1 ]

        longest_palindrome_without_first_char = memo[str_without_first_char] if str_without_first_char in memo else longest_palindrome_subseq ( string [ 1 : len(string) ] , curr_score )
        longest_palindrome_without_last_char = memo[str_without_last_char] if str_without_last_char in memo else longest_palindrome_subseq  ( string [ 0 : len(string) - 1 ], curr_score )
        
        memo [ str_without_first_char ] = longest_palindrome_without_first_char
        memo [ str_without_last_char ] = longest_palindrome_without_last_char

        return max ( longest_palindrome_without_first_char , longest_palindrome_without_last_char )

string = "abxcyba"
result = longest_palindrome_subseq ( string )
print ( result )

# LCS application : LCS ( org_str , reversed_str )
def lcs_dp ( first_string: str, second_string : str ):
    dp = [ [ 0 for _ in range (len (first_string) + 1) ] for _ in range (len (second_string) + 1) ]
    
    for first_str_index in range ( 1 , len ( first_string ) + 1 ):
        for second_str_index in range ( 1 , len ( second_string ) + 1 ):

            if first_string [ first_str_index - 1 ] == second_string [ second_str_index - 1 ]:
                dp [ first_str_index ] [ second_str_index ] = dp[first_str_index - 1] [ second_str_index - 1 ] + 1

            else:
                dp [ first_str_index ] [ second_str_index ] = max ( dp [ first_str_index - 1 ] [ second_str_index ] ,\
                                                                    dp [ first_str_index ] [ second_str_index - 1 ] )
                
    return dp [ len(first_string) ] [ len ( second_string ) ]

def longest_palindrome_subseq_dp ( string : str ):
    return lcs_dp ( string , string [ ::-1 ] )

string = "abxcyba"
result = longest_palindrome_subseq_dp ( string )
print ( result )