digits = range(1,10)

output = []

def n_digit_increasing ( n , nums = [] ):

    if n == 0:
        if nums not in output:
            output.append ( nums )
        return 
    
    for num in digits:
        if nums and nums[-1] < num:
            n_digit_increasing ( n-1 , nums + [num] )
        elif not nums:
            n_digit_increasing ( n-1 , nums + [num] )
            
n_digit_increasing ( 3 ) 
print ( output )