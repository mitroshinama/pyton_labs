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

print(f'''

[3, -1, 5, 5, 0] -> {min_max([3, -1, 5, 5, 0])}
[42] -> {min_max([42])}
[-5, -2, -9] -> {min_max([-5, -2, -9])}
[1.5, 2, 2.0, -3.1] -> {min_max([1.5, 2, 2.0, -3.1])}
''')
#print(f'[] -> {min_max([])}')
print(f'''

[3, 1, 2, 1, 3] -> {unique_sorted([3, 1, 2, 1, 3])}
[] -> {unique_sorted([])}
[-1, -1, 0, 2, 2] -> {unique_sorted([-1, -1, 0, 2, 2])}
[1.0, 1, 2.5, 2.5, 0] -> {unique_sorted([1.0, 1, 2.5, 2.5, 0])}
''')

print(f'''

[[1, 2], [3, 4]] -> {flatten([[1, 2], [3, 4]])}
[[1, 2], (3, 4, 5)] -> {flatten([[1, 2], (3, 4, 5)])}
[[1], [], [2, 3]] -> {flatten([[1], [], [2, 3]])}
''')
print(f'[[1, 2], "ab"] -> {flatten([[1, 2], "ab"])}') 
