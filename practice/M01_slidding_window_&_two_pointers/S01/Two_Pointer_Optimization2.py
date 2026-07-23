#26
from typing import List
def removeDuplicates(nums: List[int]) -> int:
    i=0
    for j in range(1,len(nums)):
        if nums[i]!=nums[j]:
            i+=1
            nums[i]=nums[j]
    return i+1
nums=[1,2,3,2,3]
print(removeDuplicates(nums))
#27
def removeElement(nums: List[int], val: int) -> int:
        i=0
        for j in range(0,len(nums)):
            if nums[j]!=val:
                nums[i]=nums[j]
                i+=1
        return i
nums=[1,2,3,2,3]
val=3
print(removeElement(nums,val))

def twoSum(numbers: List[int], target: int) -> List[int]:
        left=0
        right=len(numbers)-1

        while left<right:
            if numbers[left]+numbers[right]==target:
                return [left+1,right+1]
            elif numbers[left]+numbers[right]>target:
                right-=1
            else:
                left+=1
numbers=[2,7,11,15]
target = 9
print(twoSum(numbers,target))

def sortedSquares(nums: List[int]) -> List[int]:
        a=[]
        for i in nums:
            a.append(i**2)
        a.sort()
        return a
nums=[-4,-1,0,3,10]
print(sortedSquares(nums))

