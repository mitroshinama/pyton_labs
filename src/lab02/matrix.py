#1
def transpose(mat):
    if not mat:
        return []
    w=len(mat[0])
    for r in mat:
        if len(r) != w:
            raise ValueError("Рваная матрица")
    res=[]
    for j in range(w):
        new_r=[]
        for i in range(len(mat)):
            new_r.append(mat[i][j])
        res.append(new_r)
    return res
#2
def row_sums(mat):
    if not mat:
        return []
    w=len(mat[0])
    for r in mat:
        if len(r)!=w:
            raise ValueError("Рваная матрица")
    res=[]
    for r in mat:
        s=0
        for x in r:
            s+=x
        res.append(s)
    return res
#3
def col_sums(mat):
    if not mat:
        return []
    w=len(mat[0])
    for r in mat:
        if len(r)!=w:
            raise ValueError("Рваная матрица")
    res=[]
    for j in range(w):
        s = 0
        for i in range(len(mat)):
            s+=mat[i][j]
        res.append(s)
    return res

print(f'''
transpose

[[1, 2, 3]] -> {transpose([[1, 2, 3]])}
[[1], [2], [3]] -> {transpose([[1], [2], [3]])}
[[1, 2], [3, 4]] -> {transpose([[1, 2], [3, 4]])}
[] -> {transpose([])}
''')

#print(f'[[1, 2], [3]] -> {transpose([[1, 2], [3]])}')

print(f'''
row_sums

[[1, 2, 3], [4, 5, 6]] -> {row_sums([[1, 2, 3], [4, 5, 6]])}
[[-1, 1], [10, -10]] -> {row_sums([[-1, 1], [10, -10]])}
[[0, 0], [0, 0]] -> {row_sums([[0, 0], [0, 0]])}
''')

#print(f'[[1, 2], [3]] -> {row_sums([[1, 2], [3]])}')

print(f'''
col_sums

[[1, 2, 3], [4, 5, 6]] → {col_sums([[1, 2, 3], [4, 5, 6]])}
[[-1, 1], [10, -10]] → {col_sums([[-1, 1], [10, -10]])}
[[0, 0], [0, 0]] → {col_sums([[0, 0], [0, 0]])}
''')

print(f'[[1, 2], [3]] -> {col_sums([[1, 2], [3]])}')