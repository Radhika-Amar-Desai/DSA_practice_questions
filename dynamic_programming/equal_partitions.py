def subset_sum ( nums : list, n : int, target_sum : int ):
    if n == 0 and target_sum == 0:
        return True
    
    elif n == 0:
        return False
    
    return subset_sum ( nums, n - 1, target_sum - nums [ n - 1 ] ) or subset_sum ( nums, n - 1, target_sum )

nums = [ 1, 3, 5, 3 ]

result = sum(nums) % 2 == 0 and subset_sum ( nums, 4, sum(nums) / 2 )

print ( result )