def LIS_dp(nums: list) -> int:
    '''动态规划解法'''
    if not nums:
        return 0
    n = len(nums)
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

if __name__ == '__main__':
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    result = LIS_dp(nums)
    print(result)