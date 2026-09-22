n=int(input('in_1: '))
q=0
w=0
for i in range(n):
    a=input(f'in_{i+2}: ').split()
    if a[3]=='True':
        q+=1
    if a[3]=='False':
        w+=1
print('out:', q, w)
