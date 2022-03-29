import random

Graph = {
    1: {2: [8, 0.200],  3: [2, 0.200],  4: [20, 0.200], 5: [12, 0.200]},
    2: {1: [8, 0.200],  3: [7, 0.200],  4: [1, 0.200],  5: [15, 0.200]},
    3: {1: [2, 0.200],  2: [7, 0.200],  4: [5, 0.200],  5: [9, 0.200]},
    4: {1: [20, 0.200], 2: [1, 0.200],  3: [5, 0.200],  5: [3, 0.200]},
    5: {1: [12, 0.200], 2: [15, 0.200], 3: [9, 0.200],  4: [3, 0.200]}
}

def leng(s, g):
    l = 0
    for i in range(len(s)-1):
        for row in g:
            if row == s[i]:
                l += g[row][s[i+1]][0]
    return l


#-----константы
alph=1
betta=1
Q=1

def find_P(i,s,g):
    s1=list(s.copy())
    s1.remove(i)
    s1.insert(0,i)
    S=[]
    while len(s1)>1:
        s3=[]
        for j in range(1,len(s1)):
            k1=((1/g[s1[0]][s1[j]][0])**alph)*g[s1[0]][s1[j]][1]**betta
            k2=0
            for j1 in range(len(s1)):
                if(s1[j1]!=s1[0]):
                    k2 += ((1 / g[s1[0]][s1[j1]][0])**alph) * g[s1[0]][s1[j1]][1]**betta
            P=k1/k2
            l=[]
            l.append(P*100)
            l.append(s1[j])
            s3.append(l)

        print(s3)
        for j in range(1,len(s3)):
            s3[j][0]=s3[j-1][0]+s3[j][0]
        r=random.randint(0,99)
        if r <= s3[0][0]:
            s1.remove(s3[0][1])
            s1.pop(0)
            s1.insert(0, s3[0][1])
            S.append(s3[0][1])
        else:
            j1 = 1
            while True:
                if s3[j1-1][0]<r<=s3[j1][0]:
                    S.append(s3[j1][1])
                    s1.remove(s3[j1][1])
                    s1.pop(0)
                    s1.insert(0,s3[j1][1])
                    break
                j1 += 1
        print(S)
    S.insert(0,i)
    S.append(i)
    l = leng(S,g)
    delT=Q/l
    for i in range(len(S)-1):
        for row in g:
            if row == S[i]:
                g[row][S[i+1]][1]=round((g[row][S[i+1]][1]+delT),5)
            if row == S[i+1]:
                g[row][S[i]][1] = round((g[row][S[i]][1]+ delT),5)
    return(S)
for k in range(500):
    print('итерация №', k+1)
    s = [1, 2, 3, 4, 5]
    for i in range(1,len(s)+1):
        print('-'*30)
        s = [1, 2, 3, 4, 5]
        s=find_P(i,s,Graph)
        for row in Graph:
            print(row,Graph[row])
        print(s,leng(s,Graph))
        print('-' * 30)





