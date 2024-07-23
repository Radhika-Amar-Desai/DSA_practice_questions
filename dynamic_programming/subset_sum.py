def subset_sum ( nums : list, target_sum : int, n : int ):
    if target_sum == 0:
        return True
    
    if n == 1:
        return nums [ 0 ] == target_sum
    
    if nums [ n - 1 ] <= target_sum : 
        return subset_sum ( nums , target_sum - nums [ n - 1 ] , n - 1 ) or subset_sum ( nums , target_sum , n - 1 )
    
    if nums [ n - 1 ] > target_sum:
        return subset_sum ( nums , target_sum , n - 1 )
    
# print ( subset_sum ( [ 1, 4, 2, 3 ] , 6 , 4 ) )

def subset_sum_top_bottom ( nums : list, target_sum : int, n : int ):

    dp = [ [ _ for _ in n ] for _ in target_sum ]

    for nums_size in range ( n ):
        for sub_sum in range ( target_sum ):
            if sub_sum == 0:
                dp [ nums_size ][ sub_sum ] = True

            elif nums_size == 0:
                dp [ nums_size ][ sub_sum ] = False

    for nums_size, num in enumerate ( nums ):
        for sub_sum in range ( target_sum ):
            if sub_sum != 0 and nums_size != 0:
                dp [ nums_size ][ sub_sum ] = dp [ nums_size - 1 ][ sub_sum - num ] or dp [ nums_size - 1 ][ sub_sum ]

    return dp [ n - 1 ][ target_sum ]

result = subset_sum ( [ 1, 4, 2, 3 ], target_sum = 20, n = 4 )
print ( result )