fio=input('ФИО:').split()
fionew=''.join(fio)
ini=[]
for i in fio:
    ini.append(i[0])
print(f'Иницивлы: {''.join(ini)}.')
print('Длина (символов):', len(fionew)+2)