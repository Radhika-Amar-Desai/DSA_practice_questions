# Recursive approach
def lcs ( first_str : str, second_str : str ) -> int:
    if first_str == "" or second_str == "":
        return 0
    
    if first_str[-1] == second_str[-1]:
        return 1 + lcs ( first_str [ : -1 ] , second_str [ : -1 ] )
    
    else:
        return max ( lcs ( first_str [ : -1 ], second_str ), lcs ( first_str, second_str [ : - 1 ] ) )
    
#Memoization / Bottom Up Approach

memo = {}

def lcs_memo ( first_str , second_str ):
    if first_str == "" or second_str == "":
        return 0
    
    if first_str[-1] == second_str[-1]:
        key = ( first_str[:-1], second_str[:-1] )

        if key in memo:
            return 1 + memo [ key ]
        else:
            return 1 + lcs_memo ( first_str[:-1], second_str[:-1] )
        
    else:
        first_key = ( first_str[:-1], second_str )
        second_key = ( first_str , second_str[:-1] )

        first_lcs = memo[first_key] if first_key in memo else lcs_memo ( first_str[:-1] , second_str )
        second_lcs = memo[second_key] if second_key in memo else lcs_memo ( first_str , second_str[:-1] )

        memo [first_key] = first_lcs
        memo [second_key] = second_lcs

        return max ( first_lcs , second_lcs )

#Dynamic Programming / top down approach
def lcs_dp ( first_str, second_str ):

    dp = [ [ 0 for _ in range ( len ( second_str ) + 1 ) ] for _ in range ( len ( first_str ) + 1 ) ]
        
    for first_index in range ( 1 ,  len ( first_str ) + 1 ):
        for second_index in range ( 1 , len ( second_str ) + 1 ):
            
            first_str_char = first_str [ first_index - 1 ]
            second_str_char = second_str [ second_index - 1 ]

            if first_str_char == second_str_char:
                dp [ first_index ] [ second_index ] = 1 + dp [ first_index - 1 ] [ second_index - 1 ]

            else:
                dp [ first_index ] [ second_index ] = max ( dp [ first_index - 1 ] [ second_index ], 
                                                            dp [ first_index ] [ second_index - 1 ] )
                
    return dp [ len ( first_str ) ] [ len ( second_str ) ]


first_string = "ABCDEFGHI"
second_string = "AXBYXYZ"

result = lcs_dp ( first_string, second_string )
print ( result )