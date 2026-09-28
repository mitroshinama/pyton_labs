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

s = eval(input())     
print(transpose(s))
print(row_sums(s))
print(col_sums(s))