def min_max(nums):
    if not nums:
        raise ValueError("ValueError")
    mn=mx=nums[0]
    for x in nums:
        if x<mn:
            mn=x
        if x>mx:
            mx=x
    return mn, mx

def unique_sorted(a):
    b = []
    for x in a:
        if x not in b:
            b.append(x)
    n = len(b)
    for i in range(n):
        for j in range(n-1):
            if b[j]>b[j+1]:
                b[j],b[j+1]=b[j+1],b[j]
    return b

def flatten(mat):
    res = []
    for r in mat:
        if not isinstance(r, (list, tuple)):
            raise TypeError
        for x in r:
            res.append(x)
    return res

s = eval(input())     
print(min_max(s))
print(unique_sorted(s))
print(flatten(s))


