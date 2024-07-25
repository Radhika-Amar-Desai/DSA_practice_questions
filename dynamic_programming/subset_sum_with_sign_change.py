def findTargetSumWays(nums, target):
    from collections import defaultdict

    dp = defaultdict(int)
    dp[0] = 1

    for num in nums:
        next_dp = defaultdict(int)
        for sum_so_far in dp:
            next_dp[sum_so_far + num] += dp[sum_so_far]
            next_dp[sum_so_far - num] += dp[sum_so_far]
        dp = next_dp

    print ( dp )

    return dp[target]

# Example 1
nums1 = [1, 1, 1, 1, 1]
target1 = 3
print(findTargetSumWays(nums1, target1))  # Output: 5

# Example 2
nums2 = [1]
target2 = 1
print(findTargetSumWays(nums2, target2))  # Output: 1
