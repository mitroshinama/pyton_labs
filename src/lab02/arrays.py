def min_max(nums):
    if not nums:
        return ValueError("ValueError")
    mn=mx=nums[0]
    for x in nums:
        if x<mn:
            mn=x
        if x>mx:
            mx=x
    return mn, mx
s = eval(input())     
print(min_max(s))