import math
import random

w=0
c1=1
c2=1
s=[]
v=[]
opts=[]
opts1=[]
def h(x,y):
    f= (x - 3.14) ** 2 + (y - 2.72) ** 2 + math.sin(3 * x + 1.41) + math.sin(4 * y - 1.73)
    return f
for i in range(40):
    x=random.uniform(0,5)
    y=random.uniform(0,5)
    f = (x - 3.14) ** 2 + (y - 2.72) ** 2 + math.sin(3 * x + 1.41) + math.sin(4 * y - 1.73)
    s.append([x,y])
    opts.append([x,y])
    v.append([0,0])
min=h(s[0][0],s[0][1])
min1=0
for i in range(len(s)):
    if h(s[i][0],s[i][1])<=min:
        min=h(s[i][0],s[i][1])
        min1=i
print(min,s[min1])
while w!=50:
    p1=[]
    p2=[]
    p3=[]
    r1 = random.uniform(0, 1)
    r2 = random.uniform(0, 1)
    for j in range(len(s)):
        x = s[j][0]
        y = s[j][1]
        p1=[opts[j][0]-s[j][0],opts[j][1]-s[j][1]]
        if opts[j]<=s[j]:
            opts[j]=s[j]

        min = h(s[0][0], s[0][1])
        min1 = 0
        for i in range(len(s)):
            if h(s[i][0], s[i][1]) <= min:
                min = h(s[i][0], s[i][1])
                min1 = i
        p2=[s[min1][0]-s[j][0],s[min1][1]-s[j][1]]
        v[j]=[c1*r1*(v[j][0]+p1[0]+p2[0]),c2*r2*(v[j][1]+p1[1]+p2[1])]
        s[j]=[s[j][0]+v[j][0],s[j][1]+v[j][1]]
    for i in range(len(s)):
       if h(s[i][0], s[i][1]) <= min:
           min = h(s[i][0], s[i][1])
           min1 = i
    print(s[min1],min)
    w+=1

