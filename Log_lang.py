
array=[]
array1=[]
array2=[]
alpha=[]
d1=dict()
# разделитель между алфавитом и аксиомами
flag=0

# Считывание файла input.txt
file = open("input.txt", "r")
simvols='''
------Обозначения символов------
      -> - импликация
      |  - логическое "ИЛИ"
      &  - логическое "И"
      ~  - НЕ
--------------------------------    
'''
print(simvols)
print('-------------Алфавит------------')
def rename(d,array1):
    for i in range(len(array1)):
        if array1[i] == '-' and array1[i + 1] == '>':
            array1[i] = '->'
            array1.pop(i + 1)
            break
    array = array1.copy()
    for i in range(len(array1)):
        for j in range(len(array1)):
            for key in d:
                if key == array1[j]:
                    array1[j] = d[key]
    str=''
    for i in array:
        str+=i
    array2.append(str)
    return(array)
z=0
for line in file:
    if line.strip()=='':
        flag=1
    if flag==0:
        print(line.strip())
        f1=line.strip().split(':')
        #Заносим алфавит в словарь
        d1[f'{f1[0]}']=f1[1]

        alpha.append(f1[0])
    else:
        z+=1
        if z==1:
            print('--------------------------------')
            print(' ')
            print('-------------Аксиомы------------')
        print("             ",line.strip())
        array1 = list(line.strip())
        rename(d1,array1)
array2.pop(0)
print(' ')
print('--------------------------------')
print(' ')
print('---------Метод резолюций--------')
for i in range(len(array2)):
    array2[i]=array2[i].replace('->','|')
    if array2[i][0]=="~":
        array2[i]=array2[i].replace('~','',1)
    else:
        array2[i]='~'+array2[i]
array4=[]
array5=[]
d=[]
for i in range(len(array2)):
    d=array2[i]
    array2[i]=d.split('|')
    array5.append(d.split('|'))
print(array2)
s1=""
h='1'
def w12(array2,h1):
    for i in range(len(array2)):
        for j in range(i+1,len(array2)):
            u=[]
            o12 = list(array2[i])
            for k in range(len(array2[i])):
                if len(array2[i][k])==1:
                    array2[i][k]='~'+array2[i][k]
                elif len(array2[i][k])==2:
                    array2[i][k] = array2[i][k][1:]
            if array2[i][k] in array2[j]:
                if array2[i]==array2[j]:

                    array2[i] = o12
                    print(array2)
                    if h1==1:
                        print(o12,array2[j],' - ∅')
                    elif h1==2:
                        print(o12,' ⋂ ', array2[j], ' = ∅     =>теорема верна по методу опровержения')
                    print('--------------------------------')
                    quit()
                l1=list(set(array2[i]) & set(array2[j]))
                for h in range(len(l1)):
                    if len(l1[h]) == 1:
                        l2 = '~' + l1[h]
                    elif len(l1[h]) == 2:
                        l2 = l1[h][1:]
                    l1.append(l2)
                array2[i] = o12
                for k1 in range(len(array2[i])):
                    if array2[i][k1] not in l1:
                        u.append(array2[i][k1])
                for k1 in range(len(array2[j])):
                    if array2[j][k1] not in l1:
                        u.append(array2[j][k1])
                # print(array2[i],array2[j],u) #склейки
                if u not in array2 and u[::-1] not in array2 and len(u)>0:
                    array2.append(u)
            array2[i] = o12
    return(array2)
ki=1
array6=[]
h=1
while True:
    array6=list(array5).copy()
    if ki==1:
        array5 = w12(array5,1)
        print(array5)
    if array6 == array5:
        print('--------------------------------')
        print("Произвести склейку больше невозможно => система полна и непротиворечива")
        print('--------------------------------')
        print(' ')
        break
    else:
        array5 = w12(array5,1)
        print(array5)
    ki+=1

print('Введите теорему:')
f =list(input())
def merge(myList, a, b):
    myList[a] = myList[a] + myList.pop(b)
    return myList

for i in range(len(f)):
    if f[i-1]=='-' and  f[i]=='>':
        merge(f, i-1, i)
array2=rename(d1,f)

for i in range(len(array2)):
    if array2[i]=="->":
        for j in range(0,i):
            if i==1:
                if len(array2[j]) == 1:
                    array2[j] = '~' + array2[j]
                else:
                    array2[j - 1] = array2[j - 1][1:]
            if len(array2[j])==1:
                if array2[j] not in alpha:
                    if array2[j]=='&':
                        array2[j]='|'
                    elif array2[j]=='|':
                        array2[j]='&'
                    if len(array2[j - 1]) == 1:
                        array2[j - 1] = '~' + array2[j - 1]
                    else:
                        array2[j - 1] = array2[j - 1][1:]
                    if len(array2[j + 1]) == 1:
                        array2[j + 1] = '~' + array2[j + 1]
                    else:
                        array2[j + 1] = array2[j + 1][1:]
        array2[i]='|'

print(' ')
print('--------------------------------')
print('Преобразование имликации:',array2)
print('--------------------------------')
print(' ')
l=[]
g=[]
for j in range(len(array2)):
    if len(array2[j])==1:
        if array2[j] not in alpha:
            if array2[j]=='&':
                array2[j]='_'
                if len(array2[j - 1]) == 1:
                    array2[j - 1] = '~' + array2[j - 1]
                else:
                    array2[j - 1] = array2[j - 1][1:]
                if len(array2[j + 1]) == 1:
                    array2[j + 1] = '~' + array2[j + 1]
                else:
                    array2[j + 1] = array2[j + 1][1:]
                array2.insert(j + 2, '-')
                array2.insert(j - 1, '-')

array4=[]
for i in range(len(array2)):
    if array2[i]=='_':
        array4.append('&')
    else:
        array4.append(array2[i])
for j in range(len(array2)):
    if len(array2[j])==1:
        if array2[j] not in alpha:
            if array2[j] == '|':
                array2[j] = '&'
                if array2[j - 1]!='-':
                    if len(array2[j - 1]) == 1:
                        array2[j - 1] = '~' + array2[j - 1]
                    else:
                        array2[j - 1] = array2[j - 1][1:]
                if array2[j + 1] != '-':
                    if len(array2[j + 1]) == 1:
                        array2[j + 1] = '~' + array2[j + 1]
                    else:
                        array2[j + 1] = array2[j + 1][1:]
array4=[]

for i in range(len(array2)):
    if array2[i]!='-':
        array4.append(array2[i])
for i in range(len(array4)):
    if array4[i]=='_':
        array4[i]='|'

print('--------------------------------')
print(f'¬F(x)={array4}')
print('--------------------------------')
print(' ')

for i in range(len(array2)):
    if '_' in array2:
        array2.remove('_')
    if '-' in array2:
        array2.remove('-')
m=''

for i  in range(len(array2)):
    m+=array2[i]+","
array2=m.split('&')
for i in range(len(array2)):
    array2[i] = array2[i].split(',')
    while '' in array2[i]:
        array2[i].remove('')

for i in range(len(array2)):
    if array2[i] not in array5 and array2[i][::-1] not in array5:
        array5.append(array2[i])

print('---------Метод резолюций--------')
print(array5)
ki=1

while True:
    array6=list(array5).copy()
    if ki==1:
        array5 = w12(array5,2)
        print(array5)

    if array6 == array5:
        print(' ')
        print('--------------------------------')
        print("Произвести склейку больше невозможно => Теорема не верна")
        print('--------------------------------')
        print(' ')
        break
    else:
        array5 = w12(array5,2)
        print(array5)

    ki+=1

file.close
