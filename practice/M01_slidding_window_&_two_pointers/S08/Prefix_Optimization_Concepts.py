
#Brute-force
nums = [1,2,3,4]
res = [0] * (len(nums))
for i in range(len(nums)):
    curr_sum = 0
    for j in range(0,i+1):
        curr_sum += nums[j]
    res[i] = curr_sum
print(res)

#optimal solution
nums = [1,2,3,4]
for i in range(1,len(nums)):
    nums[i] = nums[i-1] + nums[i]
print(nums)

