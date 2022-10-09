#Задана натуральная степень k. Сформировать случайным образом список
# коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint

k = int(input("k: " ))

p = []
for k in range(k+1):
    t = randint(0,100)

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
# print( s )
fname = input("enter file name: ")
f=open(fname, "wt")
f.write(s + "\n")
f.close()