def swap_chars ( s , pt , index ):
    list_of_chars = list ( s )
    list_of_chars [ pt ] , list_of_chars [ index ] = list_of_chars [ index ] , list_of_chars [ pt ]
    return "".join ( list_of_chars )

permutations = []

def permute ( s : str, uniq_chars = [],pt = 0 ):

    if pt == len ( s ) - 1:
        permutations.append ( s )
        return 
    
    if pt == 0:
        uniq_chars = [False] * len ( s )

    for index in range ( pt, len ( s ) ):
        
        if not uniq_chars[index]:

            s = swap_chars ( s , pt , index)
            uniq_chars[index] = True

            permute ( s , uniq_chars , pt  + 1)

            s = swap_chars ( s , index , pt )
            uniq_chars[index] = False

    return permutations

# print ( len ( set ( permute ( "abcd" ) ) ) )

permutations = []

print ( permute ( "abcc" ) )
