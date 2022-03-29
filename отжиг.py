import random
import math

#----------------------------создание графа--------------------
Graph = {1:[[2,10],[3,3],[5,7],[4,20]],
         2:[[1,10],[4,12],[3,17],[5,17]],
         4:[[1,20],[3,2],[2,12],[5,8]],
         3:[[2,17],[1,3],[4,2],[5,25]],
         5:[[1,7],[4,8],[2,17],[3,25]]}
#--------------------------------------------------------------

for row in Graph:
    print(row,Graph[row])
inp=[]

#------------------------ввод отправной точки-----------------------------
f=int(input())
inp.append(f)
#-------------------------------------------------------------------------

#-------------------------генерация первоначального пути--------------------------
for i in range(5):
    c='-'
    while c in inp:
        c=random.randint(1,5)
    inp.append(c)
inp.append(f)
inp.remove('-')
#----------------------------------------------------------------------------------


#----------------------------------функция определения длины пути--------------------
def leng(inp,G):
    l=0
    for i in range(len(inp)-1):
        for row in G:
            if row==inp[i]:
                for j in range(len(G[row])):
                    if inp[i+1]==G[row][j][0]:
                        l+=G[row][j][1]
    return(l)
#--------------------------------------------------------------------------------------
T=100
fl=1
while True:
    print("итерация №", fl)
    inp1 = list(inp.copy())
    t=1
    print('-'*22)
    r1=random.randint(1,4)
    print("изнач. путь",inp1)
    while t==1:
        r2 = random.randint(1, 4)
        if r1 != r2:
            print("Индексы:",r1+1, r2+1)
            break
    inp1[r1],inp1[r2]=inp1[r2],inp1[r1]
    print("изменн. путь",inp1)
    print('-' * 22)

    l1=leng(inp, Graph)
    l2 = leng(inp1, Graph)
    if l2>l1:
        deltS=l2-l1
        T=0.5*T
        P=round((100*((math.e)**(-(round((deltS//T),100))))),100)
        print("P: ", P)
        if P>random.randint(0,100):
            inp = list(inp1.copy())
        if T<0.0002:
            print("Температура: ", T)
            print("Путь", inp)
            print("Длина пути:", leng(inp, Graph))
            break

    else:
        inp = list(inp1.copy())
    print("Температура: ",T)
    print("Путь",inp)
    print("Длина пути:",leng(inp, Graph))
    fl+=1
#[1, 2, 5, 4, 3, 1] 40
