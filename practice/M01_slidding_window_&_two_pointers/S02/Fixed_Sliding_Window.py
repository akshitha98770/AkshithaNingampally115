from typing import List

def findMaxAverage(nums: List[int], k: int) -> float:
    max_avg = float("-inf")
    n = len(nums)
    for i in range(n - k + 1):
        sub_sum = 0
        for j in range(i, k + i):
            sub_sum += nums[j]
        max_avg = max(max_avg, sub_sum)
    return max_avg / k

nums = [1, 12, -5, -6, 50, 3]
k = 4
print(findMaxAverage(nums, k))

def findMaxAverages(nums: List[int], k: int) -> float:
    current_sum = sum(nums[:k])
    max_sum = current_sum
    for i in range(k, len(nums)):
        current_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, current_sum)

    return max_sum / k


nums = [1, 12, -5, -6, 50, 3]
k = 4
print(findMaxAverages(nums, k))

        