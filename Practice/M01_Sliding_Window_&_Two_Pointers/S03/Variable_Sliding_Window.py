def minSubArrayLen(target: int, nums: List[int]) -> int:
        left=0
        min_len=float("inf")
        cur_sum=0
        for right in range(len(nums)):
            cur_sum+=nums[right]
            while cur_sum >=target:
                min_len=min(min_len,right-left+1)
                cur_sum-=nums[left]
                left+=1
        return 0 if min_len==float("inf") else min_len
target = 7
nums = [2,3,1,2,4,3]
print(minSubArrayLen(target,nums))


def numSubarrayProductLessThanK(nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        ans = 0
        cur_prod = 1
        left = 0
        for right in range(len(nums)):
            cur_prod *= nums[right]
            while cur_prod >= k:
                cur_prod //= nums[left]
                left += 1
            ans += right - left + 1
        return ans
nums = [1,2,3]
k = 0
print(numSubarrayProductLessThanK(nums,target))


def totalFruit(fruits: List[int]) -> int:
        left =0
        ans=0
        freq={}
        for right in range(len(fruits)):
            freq[fruits[right]]=freq.get(fruits[right],0)+1
            while len(freq)>2:
                freq[fruits[left]]-=1
                if freq[fruits[left]]==0:
                    del freq[fruits[left]]
                left+=1
            ans=max(ans,right-left+1)
        return ans
fruits = [1,2,1]
print(totalFruit(fruits))
