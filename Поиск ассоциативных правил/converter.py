def file(y):
    f = []
    v = open(f'{y}', 'r', encoding='ANSI')  # ______
    for line in v:
        a=[]
        f.append(line.strip("\n").split(' '))
    print(f)
    return f

fff = u'C:/Users/Рушан/Downloads/product.txt'

j = file(fff)
del(j[0])

k={}
for i in j:
    if i[0] not in k:
        k[i[0]]=[]

for i in j:
    k[i[0]].append(i[1])
for i in k:
    l=''
    for p in k[i]:
        l=l+p+', '
    l=l[:-2]
    print(f'{i}|{l}')
