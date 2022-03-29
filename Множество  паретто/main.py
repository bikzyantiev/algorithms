from openpyxl import load_workbook
import numpy as np
b = load_workbook(filename='iu.xlsx')
sheet = b.active
k = 4
x = []
def maxmin(m1):
    for h1 in range(4, 14):
        s = sheet[m1 + str(h1)].value
        op.append(s)
    print(" минимум:", min(op), '\n', "максимум:", max(op))

st = np.array([["|  |", "|1|", "|2|", "|3|", "|4|", "|5|", "|6|", "|7|", "|8|", "|9|","|10|"],
               ["|1 |", "_x_", "_x_", "_x_", "_x_", "_x_", "_x_", "_x_", "_x_", "_x_", "_x_"],
               ["|2 |", "_н_", "_x_", "_x_", "_x_", "_x_", "_x_", "_x_", "_x_", "_x_", "_x_"],
               ["|3 |", "_н_", "_н_", "_x_", "_x_", "_x_", "_x_", "_x_", "_x_", "_x_", "_x_"],
               ["|4 |", "_н_", "_н_", "_н_", "_x_", "_x_", "_x_", "_x_", "_x_", "_x_", "_x_"],
               ["|5 |", "_н_", "_н_", "_н_", "_н_", "_x_", "_x_", "_x_", "_x_", "_x_", "_x_"],
               ["|6 |", "_н_", "_н_", "_н_", "_н_", "_н_", "_x_", "_x_", "_x_", "_x_", "_x_"],
               ["|7 |", "_н_", "_н_", "_н_", "_н_", "_н_", "_н_", "_x_", "_x_", "_x_", "_x_"],
               ["|8 |", "_н_", "_н_", "_н_", "_н_", "_н_", "_н_", "_н_", "_x_", "_x_", "_x_"],
               ["|9 |", "_н_", "_н_", "_н_", "_н_", "_н_", "_н_", "_н_", "_н_", "_x_", "_x_"],
               ["|10|", "_н_", "_н_", "_н_", "_н_", "_н_", "_н_", "_н_", "_н_", "_н_", "_x_"]], str)
x5 = []
data = []
data1 = []
op = []
op1 = []
inp = []
inp1 = []
for j in range(4, 14):
    s = sheet['C' + str(j)].value
    d = sheet['D' + str(j)].value
    e = sheet['E' + str(j)].value
    f = sheet['F' + str(j)].value
    g = sheet['G' + str(j)].value
    h = sheet['H' + str(j)].value
    k = k + 1
    for i in range(k, 14):
        y = sheet['C' + str(i)].value
        m = sheet['D' + str(i)].value
        v = sheet['E' + str(i)].value
        o = sheet['F' + str(i)].value
        p = sheet['G' + str(i)].value
        w = sheet['H' + str(i)].value
        if y <= s and m >= d and v >= e and o >= f and p <= g and w <= h and (y < s or m > d or v > e or o > f or p < g or w < h):
            x.append(i-3)
            x5.append(j-3)
            data.append(i-3)
            data1.append(j-3)
z6 = len(x)
print("\n")
for i in range(12):
    for j in range(12):
        if z6 != 1:
            if i == x5[0]:
                if j == x[0]:
                    z6 = len(x)
                    r3 = str(x[0])
                    f8 = "A" + r3
                    l8 = 3 - len(f8)
                    st[x[0]][x5[0]] = f8 + l8*"_"
                    x5.pop(0)
                    x.pop(0)



res = list(set(data))
res1 = list(set(data1))
x1 = list(res)
x6 = list(res1)
x1.sort()
d1 = []
uu =[]
uu1 =[]
uu2 =[]
uu3 =[]
uu4 =[]
uu5 =[]
uu6 =[]

print(st)
print(f'\nПарето-оптимальные варианты:{x1}')
print(f'Доминируемые варианты:{x6}')
print(f'выберете один из вариантов сужения:\n1)указание верхних/нижних границ\n2)субоптимизация\n3)лексикографический')
y9 = int(input())

if y9 == 1:
    x7=[1,2,3,4,5,6,7,8,9,10]
    #указание верхних нижних границ
    while len(x7)!=1:
        result = x7
        print('укажите номера выбранных вами критериев(колличество критериев не более 6) в виде:"1 4 6"')
        d2 = input()
        inp = [int(a) for a in d2.split()]
        for i in range(len(inp)):
            while (inp[i]>6):
                print(f'введите соответствующее условию значение вместо значения:{inp[i]}')
                inp[i]=int(input())
                while (inp[i] <= 0):
                    print(f'введите соответствующее условию значение вместо значения:{inp[i]}')
                    inp[i] = int(input())
            while (inp[i]<=0):
                print(f'введите соответствующее условию значение вместо значения:{inp[i]}')
                inp[i]=int(input())
                while (inp[i] > 6):
                    print(f'введите соответствующее условию значение вместо значения:{inp[i]}')
                    inp[i] = int(input())
            i=0
        print(f'ваш выбор:{inp}')
        for i in range(len(inp)):
            up = inp[i]
            if up == 1:
                m1 = 'C'
                print('Цена:')
                maxmin(m1)
                print('введите верхние и нижние границы, входящие в промежуток:')
                d3 = input()
                inp1 = [int(a) for a in d3.split()]
                for i in range(len(inp1)):
                    while (max(op) < inp1[i] or inp1[i] < min(op)):
                        print(f'введите соответствующее условию значение вместо значения:{inp1[i]}')
                        inp1[i] = int(input())
                    i = 0
                print(f'ваш выбор:{inp1}')
                for h1 in range(4, 14):
                    s = sheet[m1 + str(h1)].value
                    if inp1[0] <= s <= inp1[1]:
                        uu1.append(h1-3)
                result = uu1
                print(result)
                op.clear()
            if up == 2:
                m1 = 'D'
                print('Частота работы видеочипа:')
                maxmin(m1)
                print('введите верхние и нижние границы, входящие в промежуток:')
                d3 = input()
                inp1 = [int(a) for a in d3.split()]
                for i in range(len(inp1)):
                    while (max(op) < inp1[i] or inp1[i] < min(op)):
                        print(f'введите соответствующее условию значение вместо значения:{inp1[i]}')
                        inp1[i] = int(input())
                    i = 0
                print(f'ваш выбор:{inp1}')
                for h1 in range(4, 14):
                    s = sheet[m1 + str(h1)].value
                    if inp1[0] <= s <= inp1[1]:
                        uu2.append(h1-3)
                result = list(set(uu2) & set(result))
                print(result)
                op.clear()
            if up == 3:
                m1 = 'E'
                print('пропусканая способность:')
                maxmin(m1)
                print('введите верхние и нижние границы, входящие в промежуток:')
                d3 = input()
                inp1 = [int(a) for a in d3.split()]
                for i in range(len(inp1)):
                    while (max(op) < inp1[i] or inp1[i] < min(op)):
                        print(f'введите соответствующее условию значение вместо значения:{inp1[i]}')
                        inp1[i] = int(input())
                    i = 0
                print(f'ваш выбор:{inp1}')
                for h1 in range(4, 14):
                    s = sheet[m1 + str(h1)].value
                    if inp1[0] <= s <= inp1[1]:
                        uu3.append(h1-3)
                result = list(set(result) & set(uu3))
                print(result)
                op.clear()
            if up == 4:
                m1 = 'F'
                print('объем памяти:')
                maxmin(m1)
                print('введите верхние и нижние границы, входящие в промежуток:')
                d3 = input()
                inp1 = [int(a) for a in d3.split()]
                for i in range(len(inp1)):
                    while (max(op) < inp1[i] or inp1[i] < min(op)):
                        print(f'введите соответствующее условию значение вместо значения:{inp1[i]}')
                        inp1[i] = int(input())
                    i = 0
                print(f'ваш выбор:{inp1}')
                for h1 in range(4, 14):
                    s = sheet[m1 + str(h1)].value
                    if inp1[0] <= s <= inp1[1]:
                        uu4.append(h1-3)
                result = list(set(result) & set(uu4))
                print(result)
                op.clear()
            if up == 5:
                m1 = 'G'
                print('длина:')
                maxmin(m1)
                print('введите верхние и нижние границы, входящие в промежуток:')
                d3 = input()
                inp1 = [int(a) for a in d3.split()]
                for i in range(len(inp1)):
                    while (max(op) < inp1[i] or inp1[i] < min(op)):
                        print(f'введите соответствующее условию значение вместо значения:{inp1[i]}')
                        inp1[i] = int(input())
                    i = 0
                print(f'ваш выбор:{inp1}')
                for h1 in range(4, 14):
                    s = sheet[m1 + str(h1)].value
                    if inp1[0] <= s <= inp1[1]:
                        uu5.append(h1-3)
                result = list(set(result) & set(uu5))
                print(result)
                op.clear()
            if up == 6:
                m1 = 'H'
                print('ширина:')
                maxmin(m1)
                print('введите верхние и нижние границы, входящие в промежуток:')
                d3 = input()
                inp1 = [int(a) for a in d3.split()]
                for i in range(len(inp1)):
                    while (max(op) < inp1[i] or inp1[i] < min(op)):
                        print(f'введите соответствующее условию значение вместо значения:{inp1[i]}')
                        inp1[i] = int(input())
                    i = 0
                print(f'ваш выбор:{inp1}')
                for h1 in range(4, 14):
                    s = sheet[m1 + str(h1)].value
                    if inp1[0] <= s <= inp1[1]:
                        uu6.append(h1-3)
                result = list(set(result) & set(uu6))
                print(result)
                op.clear()
        k=0
        x8 = []
        x7 = []
        x9 = []
        for j in range(len(result)):
            s4 = sheet['C' + str(result[j]+3)].value
            d4 = sheet['D' + str(result[j]+3)].value
            e4 = sheet['E' + str(result[j]+3)].value
            f4 = sheet['F' + str(result[j]+3)].value
            g4 = sheet['G' + str(result[j]+3)].value
            h4 = sheet['H' + str(result[j]+3)].value
            k4 = k + 1
            for i in range(k,len(result)):
                y4 = sheet['C' + str(result[i]+3)].value
                m4 = sheet['D' + str(result[i]+3)].value
                v4 = sheet['E' + str(result[i]+3)].value
                o4 = sheet['F' + str(result[i]+3)].value
                p4 = sheet['G' + str(result[i]+3)].value
                w4 = sheet['H' + str(result[i]+3)].value
                if y4 <= s4 and m4 >= d4 and v4 >= e4 and o4 >= f4 and p4 <= g4 and w4 <= h4 and (y4 < s4 or m4 > d4 or v4 > e4 or o4 > f4 or p4 < g4 or w4 < h4):
                    x7.append(result[i])
                    x9.append(result[i])
                    x8.append(result[j])
                elif y4 >= s4 and m4 <= d4 and v4 <= e4 and o4 <= f4 and p4 >= g4 and w4>= h4 and (y4 > s4 or m4 > d4 or v4 < e4 or o4 < f4 or p4 > g4 or w4 > h4):
                    x7.append(result[j])
                    x9.append(result[j])
                    x8.append(result[i])
        x7=sorted(set(x7))
        print(x9)
        print(x8)
        print(f'парето-оптимальные вариант(ы) после сужения с указанием границ:{x7}')
if y9 == 2:
    print('укажите номер главного критерия')
    m8 = int(input())
    if m8 == 1:
        m9 = 'C'
    elif m8 == 2:
        m9='D'
    elif  m8 == 3:
        m9 = 'E'
    elif m8 == 4:
        m9 = 'F'
    elif m8 == 5:
        m9 = 'G'
    elif m8 == 6:
        m9 = 'H'
    l9=[]
    l10=[]
    for i in range(4, 14):
        l9.append(sheet[m9 + str(i)].value)
    if m8 == 1 or m8 == 5 or m8== 6:
        k0 = min(l9)
    elif m8== 2 or m8==3 or m8==4:
        k0 = max(l9)
    for i in range(4, 14):
        if k0 == sheet[m9 + str(i)].value:
            l10.append(i - 3)
    print(l10)
    result = l10
    l11=[]
    while len(result) != 1:
        l11 = result
        print(l11)
        print('укажите номера выбранных вами критериев(колличество критериев не более 6) в виде:"1 4 6"')
        d2 = input()
        inp = [int(a) for a in d2.split()]
        for i in range(len(inp)):
            while (inp[i] > 6):
                print(f'введите соответствующее условию значение вместо значения:{inp[i]}')
                inp[i] = int(input())
                while (inp[i] <= 0):
                    print(f'введите соответствующее условию значение вместо значения:{inp[i]}')
                    inp[i] = int(input())
            while (inp[i] <= 0):
                print(f'введите соответствующее условию значение вместо значения:{inp[i]}')
                inp[i] = int(input())
                while (inp[i] > 6):
                    print(f'введите соответствующее условию значение вместо значения:{inp[i]}')
                    inp[i] = int(input())
            i = 0
        print(f'ваш выбор:{inp}')
        for i in range(len(inp)):
            up = inp[i]
            if up == 1:
                m1 = 'C'
                print('Цена:')
                maxmin(m1)
                print('введите верхние и нижние границы, входящие в промежуток:')
                d3 = input()
                inp1 = [int(a) for a in d3.split()]
                for i in range(len(inp1)):
                    while (max(op) < inp1[i] or inp1[i] < min(op)):
                        print(f'введите соответствующее условию значение вместо значения:{inp1[i]}')
                        inp1[i] = int(input())
                    i = 0
                print(f'ваш выбор:{inp1}')
                for h1 in range(4, 14):
                    s = sheet[m1 + str(h1)].value
                    if inp1[0] <= s <= inp1[1]:
                        uu1.append(h1 - 3)
                result = list(set(uu1) & set(l11))
                print(result)
                op.clear()
            if up == 2:
                m1 = 'D'
                print('Частота работы видеочипа:')
                maxmin(m1)
                print('введите верхние и нижние границы, входящие в промежуток:')
                d3 = input()
                inp1 = [int(a) for a in d3.split()]
                for i in range(len(inp1)):
                    while (max(op) < inp1[i] or inp1[i] < min(op)):
                        print(f'введите соответствующее условию значение вместо значения:{inp1[i]}')
                        inp1[i] = int(input())
                    i = 0
                print(f'ваш выбор:{inp1}')
                for h1 in range(4, 14):
                    s = sheet[m1 + str(h1)].value
                    if inp1[0] <= s <= inp1[1]:
                        uu2.append(h1 - 3)
                result = list(set(uu2) & set(result))
                print(result)
                op.clear()
            if up == 3:
                m1 = 'E'
                print('пропусканая способность:')
                maxmin(m1)
                print('введите верхние и нижние границы, входящие в промежуток:')
                d3 = input()
                inp1 = [int(a) for a in d3.split()]
                for i in range(len(inp1)):
                    while (max(op) < inp1[i] or inp1[i] < min(op)):
                        print(f'введите соответствующее условию значение вместо значения:{inp1[i]}')
                        inp1[i] = int(input())
                    i = 0
                print(f'ваш выбор:{inp1}')
                for h1 in range(4, 14):
                    s = sheet[m1 + str(h1)].value
                    if inp1[0] <= s <= inp1[1]:
                        uu3.append(h1 - 3)
                result = list(set(result) & set(uu3))
                print(result)
                op.clear()
            if up == 4:
                m1 = 'F'
                print('объем памяти:')
                maxmin(m1)
                print('введите верхние и нижние границы, входящие в промежуток:')
                d3 = input()
                inp1 = [int(a) for a in d3.split()]
                for i in range(len(inp1)):
                    while (max(op) < inp1[i] or inp1[i] < min(op)):
                        print(f'введите соответствующее условию значение вместо значения:{inp1[i]}')
                        inp1[i] = int(input())
                    i = 0
                print(f'ваш выбор:{inp1}')
                for h1 in range(4, 14):
                    s = sheet[m1 + str(h1)].value
                    if inp1[0] <= s <= inp1[1]:
                        uu4.append(h1 - 3)
                result = list(set(result) & set(uu4))
                print(result)
                op.clear()
            if up == 5:
                m1 = 'G'
                print('длина:')
                maxmin(m1)
                print('введите верхние и нижние границы, входящие в промежуток:')
                d3 = input()
                inp1 = [int(a) for a in d3.split()]
                for i in range(len(inp1)):
                    while (max(op) < inp1[i] or inp1[i] < min(op)):
                        print(f'введите соответствующее условию значение вместо значения:{inp1[i]}')
                        inp1[i] = int(input())
                    i = 0
                print(f'ваш выбор:{inp1}')
                for h1 in range(4, 14):
                    s = sheet[m1 + str(h1)].value
                    if inp1[0] <= s <= inp1[1]:
                        uu5.append(h1 - 3)
                result = list(set(result) & set(uu5))
                print(result)
                op.clear()
            if up == 6:
                m1 = 'H'
                print('ширина:')
                maxmin(m1)
                print('введите верхние и нижние границы, входящие в промежуток:')
                d3 = input()
                inp1 = [int(a) for a in d3.split()]
                for i in range(len(inp1)):
                    while (max(op) < inp1[i] or inp1[i] < min(op)):
                        print(f'введите соответствующее условию значение вместо значения:{inp1[i]}')
                        inp1[i] = int(input())
                    i = 0
                print(f'ваш выбор:{inp1}')
                for h1 in range(4, 14):
                    s = sheet[m1 + str(h1)].value
                    if inp1[0] <= s <= inp1[1]:
                        uu6.append(h1 - 3)
                result = list(set(result) & set(uu6))
                print(result)
                op.clear()
        uu6=[]
        uu1=[]
        uu2=[]
        uu3=[]
        uu4=[]
        uu5=[]
if y9 == 3:
    print('укажите номер главного критерия')
    m8 = int(input())
    if m8 == 1:
        m9 = 'C'
    elif m8 == 2:
        m9 = 'D'
    elif m8 == 3:
        m9 = 'E'
    elif m8 == 4:
        m9 = 'F'
    elif m8 == 5:
        m9 = 'G'
    elif m8 == 6:
        m9 = 'H'
    l9 = []
    l10 = []
    for i in range(4, 14):
        l9.append(sheet[m9 + str(i)].value)
    if m8 == 1 or m8 == 5 or m8 == 6:
        k0 = min(l9)
    elif m8 == 2 or m8 == 3 or m8 == 4:
        k0 = max(l9)
    for i in range(4, 14):
        if k0 == sheet[m9 + str(i)].value:
            l10.append(i - 3)
    print(l10)
    result = l10
    l11=[]
    result1=[]
    while len(result) != 1:
        l9 = []
        l11=result
        print('укажите номер следующего по важности критерия')
        m8 = int(input())
        if m8 == 1:
            m9 = 'C'
        elif m8 == 2:
            m9 = 'D'
        elif m8 == 3:
            m9 = 'E'
        elif m8 == 4:
            m9 = 'F'
        elif m8 == 5:
            m9 = 'G'
        elif m8 == 6:
            m9 = 'H'
        for i in range(len(result)):
            l9.append(sheet[m9 + str(result[i]+3)].value)
        if m8 == 1 or m8 == 5 or m8 == 6:
            k0 = min(l9)
        elif m8 == 2 or m8 == 3 or m8 == 4:
            k0 = max(l9)
        for i in range(4, 14):
            if k0 == sheet[m9 + str(i)].value:
                result1.append(i - 3)
        result = list(set(result1) & set(l11))
        print(result)
        result1=[]