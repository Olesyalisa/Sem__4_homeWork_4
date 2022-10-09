#Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

import re

def setPow(a, pow, v):
    while (len(a) <= pow):
        a.append(0)
    a[pow] = v

def parsePoly(s):
    ss = re.split( "=", s)
    if (len(ss) != 2):
        print(s + " is not and equation")
        return None

    if (ss[1].strip() != "0"):
        print("right part of " + s + " is not 0")
        return None

    ss = re.split("\\+", ss[0].strip())

    poly = []

    for sss in ss:
        sss = sss.strip()
        r = re.match('(\d+)\*x\^(\d+)', sss)
        if (r): # полная степень
            setPow(poly, int(r[2]), int(r[1]))
        else:
            r = re.match('(\d+)\*x', sss)
            if (r): # 5*x
                setPow(poly, 1, int(r[1]))
            else:
                re.match( 'x\^(\d+)', sss)
                if (r): # x^5
                    setPow(poly, int(r[1]), 1)
                else: # число
                    setPow(poly, 0, int(sss))

    return poly

fname = input("enter first file: ")
f = open(fname, "rt")
p1 = f.readline()
f.close()

poly1 = parsePoly(p1)

fname = input("enter second file: ")
f = open(fname, "rt")
p2 = f.readline()
f.close()

poly2 = parsePoly(p2)

r = []
i = 0
while (i < len(poly1)) or (i < len(poly2)):
    t = 0
    if (i < len(poly1)):
        t = t + poly1[i]
    if (i < len(poly2)):
        t = t + poly2[i]

    r.append(t)
    i += 1

p = []
for k in range(len(r)):
    t = r[k]
    if (t == 0):
        continue

    if (k == 0):
        s = ""
    elif (k == 1):
        s = "x"
    else:
        s = "x^" + str(k)

    if (t > 1):
        if (k == 0):
            s = str(t)
        else:
            s = str(t) + "*" + s

    p.insert(0, s)

s = " + ".join(p) + " = 0"
print(s)

