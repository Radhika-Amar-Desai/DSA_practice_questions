def lcs_dp ( first_str, second_str ):

    dp = [ [ "" for _ in range ( len ( second_str ) + 1 ) ] for _ in range ( len ( first_str ) + 1 ) ]
        
    for first_index in range ( 1 ,  len ( first_str ) + 1 ):
        for second_index in range ( 1 , len ( second_str ) + 1 ):
            
            first_str_char = first_str [ first_index - 1 ]
            second_str_char = second_str [ second_index - 1 ]

            if first_str_char == second_str_char and first_str_char not in dp[ first_index - 1 ][ second_index - 1 ]:
                dp [ first_index ] [ second_index ] = first_str_char + dp [ first_index - 1 ] [ second_index - 1 ]

            else:
                candidates = [ dp [ first_index - 1 ] [ second_index ], dp [ first_index ] [ second_index - 1 ]  ]
                dp [ first_index ] [ second_index ] = max ( candidates , key = lambda x : len(x) )
                
    return dp [ len ( first_str ) ] [ len ( second_str ) ][::-1]

def substract_strings ( a , b ):
    for index in range (  0, len ( a ) , 2 ):
        if ( a [ index : index + 2 ] == b ):
            return a [ : index ]
        
    return a

a = "geek"
b = "eke"

sub_seq = lcs_dp ( a , b )
print ( sub_seq )

result = substract_strings ( a , sub_seq ) + b
print ( result ) 