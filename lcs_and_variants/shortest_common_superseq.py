def lcs_dp ( first_str, second_str ):

    dp = [ [ "" for _ in range ( len ( second_str ) + 1 ) ] for _ in range ( len ( first_str ) + 1 ) ]
        
    for first_index in range ( 1 ,  len ( first_str ) + 1 ):
        for second_index in range ( 1 , len ( second_str ) + 1 ):
            
            first_str_char = first_str [ first_index - 1 ]
            second_str_char = second_str [ second_index - 1 ]

            if first_str_char == second_str_char:
                dp [ first_index ] [ second_index ] = first_str_char + dp [ first_index - 1 ] [ second_index - 1 ]

            else:
                candidates = [ dp [ first_index - 1 ] [ second_index ], dp [ first_index ] [ second_index - 1 ]  ]
                dp [ first_index ] [ second_index ] = max ( candidates , key = lambda x : len(x) )
                
    return len ( dp [ len ( first_str ) ] [ len ( second_str ) ] )

def scs ( first_str, second_str ):
    return len ( first_str ) + len(second_str) - lcs_dp ( first_str , second_str )