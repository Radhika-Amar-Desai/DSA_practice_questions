def lcs_dp ( first_str, second_str ):

    dp = [ [ 0 for _ in range ( len ( second_str ) + 1 ) ] for _ in range ( len ( first_str ) + 1 ) ]
        
    for first_index in range ( 1 ,  len ( first_str ) + 1 ):
        for second_index in range ( 1 , len ( second_str ) + 1 ):
            
            first_str_char = first_str [ first_index - 1 ]
            second_str_char = second_str [ second_index - 1 ]

            if first_str_char == second_str_char:
                dp [ first_index ] [ second_index ] = 1 + dp [ first_index - 1 ] [ second_index - 1 ]

            else:
                dp [ first_index ] [ second_index ] = 0

    print ( dp )        
    return max ( [ val for row in dp for val in row ] )

a = "abc"
b = "abxyzabc"

result = lcs_dp ( a , b )
print ( result )