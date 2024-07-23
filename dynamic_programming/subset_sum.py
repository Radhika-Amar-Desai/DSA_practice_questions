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

    dp = [ [ 0 for _ in range(target_sum + 1) ] for _ in range(n + 1) ]

    for nums_size in range ( n + 1):
        for sub_sum in range ( target_sum + 1 ):
            if sub_sum == 0:
                dp [ nums_size ][ sub_sum ] = 1

            elif nums_size == 0:
                dp [ nums_size ][ sub_sum ] = 0

    print ( dp )

    for nums_size in range ( 1 , n + 1 ):
        for sub_sum in range ( 1 , target_sum + 1 ):
            if sub_sum > 0 and nums_size > 0 and nums[nums_size - 1] <= sub_sum:
                dp [ nums_size ][ sub_sum ] = dp [ nums_size - 1 ][ sub_sum - nums [ nums_size - 1 ] ] + dp [ nums_size - 1 ][ sub_sum ]

            else:
                dp[ nums_size ][ sub_sum ] = dp [ nums_size - 1 ][ sub_sum ]

    print ( dp )

    return dp [ n ][ target_sum ]

result = subset_sum_top_bottom ( [ 2, 5 , 3 , 4 ], target_sum = 6, n = 4 )
print ( result )