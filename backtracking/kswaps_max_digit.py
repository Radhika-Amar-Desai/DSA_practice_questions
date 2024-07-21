swaps = set()

def swap(s, index1, index2):
    chars = list(s)
    chars[index1], chars[index2] = chars[index2], chars[index1]
    return "".join(chars)

def kswaps ( s , k , swap_no = 0 ):
    if k == swap_no:
        swaps.add ( int(s) )
        return int(s)
    
    for first_index in range ( len ( s ) - 1 ):
        for second_index in range ( first_index + 1, len(s) ):
                
                s = swap ( s , first_index, second_index )
                print(kswaps ( s, k, swap_no + 1 ),swap_no)
                s = swap ( s , second_index, first_index )

kswaps ( "1234", 1 )
print ( swaps )