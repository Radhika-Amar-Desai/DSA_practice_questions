digits = range ( 1 , 10 )

n_digit_nums_increasing = []

def add_digit_at_nth_place ( s , n , digit ):

    chars = list ( s )
    chars [ len(s) - n ] = str ( digit )

    return "".join ( chars )

def remove_digit_from_nth_place ( s , n ):
    chars = list ( s )
    chars [ len ( s ) - n  ] = '0'

    return "".join ( chars )

def n_digit_increasing ( n : int , s : str ):
    if n == 0:
        n_digit_nums_increasing.append ( s )
        return 
    
    for digit in range ( 1, 10 ) :
        
        if int ( s [ 0 ] ) < digit:
                s = add_digit_at_nth_place ( s , n, digit )
                n_digit_increasing ( n - 1, s )
                s = remove_digit_from_nth_place ( s , n )

n_digit_increasing ( 3, '000' )

print ( n_digit_nums_increasing )