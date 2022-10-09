#Вычислить число c заданной точностью d
# Пример: при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

def numPi(form=1.0e-5):
    num = 0
    d = 1
    two = 1
    while True:
        i = 4 / d
        num += two * i
        if i<form:
            return num
        two = -two
        d += 2
print(f'the numbers PI is equal to {round(numPi(),4)}')