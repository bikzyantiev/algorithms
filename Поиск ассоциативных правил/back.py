from itertools import combinations

o1 = []
o4 = []
f = []

S = 5  # ______

# inp='по условию'#_____
inp = 'по следствию'  # _____


def file(y):
    f = []
    v = open(f'{y}', 'r', encoding='ANSI')  # ______
    for line in v:
        f.append(line.strip("\n").split('|')[1])
    del f[0]
    print(f)
    return f


def file1(y):
    f1 = []
    v = open(f'{y}', 'r', encoding='ANSI')  # ______
    for line in v:
        f1.append(line.strip("\n").split('|'))
    print(f1)
    return f1


def popul(f, minp, maxp):
    mn = []
    for line in f:
        for el in (line.split(', ')):
            if el not in mn:
                mn.append(el)
    a1 = []
    for line in f:
        a = []
        for el in (line.split(', ')):
            a.append(el)
        a1.append(a)
    o = []
    col = 0
    ip = {col: 0}
    for i in range(1, S):
        k = set(combinations(mn, i))
        for l in k:
            for line in a1:
                u = []
                for p in range(len(l)):
                    if l[p] in line:
                        u.append('t')
                    else:
                        u.append('f')
                if 'f' not in u:
                    if l not in o:
                        o.append(l)  # сюда можно добавить колличество повторов
                        col = 1
                    else:
                        col += 1
                    ip[l] = col
    o1 = []

    for i in range(len(o)):
        c = 0
        g = {'line': [], 'p': 0, 'col': 0}

        for j in range(len(a1)):
            k = []
            for z in range(len(o[i])):
                if o[i][z] in a1[j]:
                    k.append('t')
                else:
                    k.append('f')
            if 'f' not in k:
                c += 1  # подсчет колл-ва повторов в транзакциях
        if minp <= int(c / len(a1) * 100) <= maxp:
            g['line'] = o[i]
            g['p'] = c / len(a1) * 100  # подсчет поддержки множества
            g['col'] = ip[o[i]]
            o1.append(g)
    return o1


def rules(o1, f, minp, maxp, mind, maxd):
    print('------------------------------правила----------------------------------------')
    rul = []
    rul2 = []
    a1 = []
    for line in f:
        a = []
        for el in (line.split(', ')):
            a.append(el)
        a1.append(a)
    print(a1)
    for y in range(len(o1)):
        for y1 in range(len(o1)):
            rul1 = {'r1': [], 'r2': [], 'p': 0, 'd': 0, 'lift': 0, 'c': 0, 'a1': 0}
            if y != y1:
                k = []
                for u in o1[y]['line']:
                    if u not in o1[y1]['line']:
                        k.append('t')
                    else:
                        k.append('f')
                if 'f' not in k and (len(o1[y]['line']) + len(o1[y1]['line'])) < S:
                    for v in a1:
                        k = []
                        h = list(o1[y]['line']).copy()
                        h1 = list(o1[y1]['line']).copy()
                        for el in (h + h1):
                            if el in v:
                                k.append('t')
                            else:
                                k.append('f')
                        if 'f' not in k:
                            rul1['r1'] = o1[y]['line']
                            rul1['r2'] = o1[y1]['line']
                            break
                else:
                    continue
            rul.append(rul1)
    for b in rul:
        if len(b['r1']) > 0:
            rul2.append(b)

    o4 = []
    for rul1 in rul2:
        c = 0
        c1 = 0
        c2 = 0
        for j in range(len(a1)):
            k = []
            for z in range(len(rul1['r1'] + rul1['r2'])):
                if (rul1['r1'] + rul1['r2'])[z] in a1[j]:
                    k.append('t')
                else:
                    k.append('f')
            if 'f' not in k:
                c += 1  # подсчет колл-ва повторов в транзакциях
            k1 = []
            for z in range(len(rul1['r1'])):
                if (rul1['r1'])[z] in a1[j]:
                    k1.append('t')
                else:
                    k1.append('f')
            if 'f' not in k1:
                c1 += 1  # подсчет колл-ва повторов в транзакциях
            k2 = []
            for z in range(len(rul1['r2'])):
                if (rul1['r2'])[z] in a1[j]:
                    k2.append('t')
                else:
                    k2.append('f')
            if 'f' not in k2:
                c2 += 1  # подсчет колл-ва повторов в транзакциях
        if minp <= (c / len(a1) * 100) <= maxp and mind <= (c / c1 * 100) <= maxd:
            rul1['p'] = c / len(a1) * 100  # подсчет поддержки множества
            # rul1['d'] = c1
            rul1['d'] = c / c1 * 100  # подсчет достоверности множества
            rul1['lift'] = (c / c1) / (c2 / len(a1))
            rul1['c'] = c
            rul1['a1'] = len(a1)
            o4.append(rul1)
    for b in o4:
        print(b)
    print(len(o4))
    print('------------------------------------------------------------------------------')
    return o4


def tree_rules(o4):
    r1 = 'r2'
    r2 = 'r1'
    o5 = []
    bd = []
    for i in range(len(o4)):
        if o4[i][r1] not in bd:
            bd.append(o4[i][r1])
        if o4[i][r2] not in bd:
            bd.append(o4[i][r2])
    print(len(bd))
    o5 = {}
    for i in bd:
        o5[i] = []
    h = {}
    # for t in o5:
    #     print(t,o5[t])
    for m in o4:
        h1 = []
        if m[r1] in o5:
            h1.append(m[r1])
            h1.append(m['p'])
            h1.append(m['d'])
            h1.append(m['lift'])
        o5[m[r2]].append(h1)

    for t in o5:
        print(t, o5[t])
    return(o5)

def what_if(o1, m, f, minp, maxp, mind, maxd):
    o8 = []
    a1 = []
    for line in f:

        a = []
        for el in (line.split(', ')):
            a.append(el)
        a1.append(a)

    e = []
    rul1 = {'r1': [], 'r2': [], 'p': 0, 'col': 0, 'd': 0, 'lift': 0}
    for i in range(len(o1)):
        for j in range(len(o1)):
            if i + 1 != j and i != j:
                if len(o1[i]['line'][0]) <= len(o1[j]['line'][0]) and i != len(o1) - 1:
                    o1[i]['line'], o1[j]['line'] = o1[j]['line'], o1[i]['line']
                else:
                    continue
    pl1 = []
    for y in o1:
        fl = []
        for y1 in m:
            if y1 not in y['line']:
                fl.append('t')
            else:
                fl.append('f')
        if 'f' not in fl:
            rul1['r1'] = m
            rul1['r2'] = list(y['line'])

        if rul1.copy() not in pl1 and len(rul1.copy()['r1']) > 0:
            pl1.append(rul1.copy())
    for rul1 in pl1:
        for z in rul1['r1']:
            c7 = 0
            c9=0
            c6 = 0
            z1 = []
            z1.append(z)
            for t in a1:
                if z in t:
                    c7 += 1

            for j in range(len(a1)):
                ke = []
                for l in (z1 + rul1['r2']):
                    if l in a1[j]:
                        ke.append('t')
                    else:
                        ke.append('f')
                if 'f' not in ke:
                    c6 += 1

                ke1=[]
                for z2 in rul1['r2']:
                    if z2 in a1[j]:
                        ke1.append('t')
                    else:
                        ke1.append('f')
                if 'f' not in ke1:
                    c9 += 1  # подсчет колл-ва повторов в транзакциях
            if minp <= (c6 / len(a1) * 100) <= maxp and mind <= (c6 / c7 * 100) <= maxd:
                rul1['p'] = c6 / len(a1) * 100  # подсчет поддержки множества
                rul1['d'] = (rul1['p'] * len(a1)) / c7  # подсчет достоверности множества
                rul1['lift'] = (c6 / c7) / (c9 / len(a1))
                rul1['col'] = c6
                if rul1.copy() not in o8:
                    o8.append(rul1.copy())

    for ty in o8:
        print(ty)
    return(o8)
'''
y = 'file.txt'
fi = file(y)
minp = 13  # ______
maxp = 100  # ______
mind = 60  # ______
maxd = 100  # ______
o7 = popul(fi, minp, maxp)
print('------------------------------популярные наборы----------------------------------------')
for i in o7:
    print(i)
o4 = rules(o7, fi, minp, maxp, mind, maxd)
print('------------------------------дерево----------------------------------------')
tree_rules(o4)
print('\n' * 2)
m = ['форсаж', 'форсаж 2']
print('-------------------------------что если----------------------------------------')
o12 = popul(fi, minp, maxp)
what_if(o12, m, fi, minp, maxp, mind, maxd)
'''