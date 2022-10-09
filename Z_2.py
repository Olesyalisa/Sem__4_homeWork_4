#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = int(input("Enter n: "))

def isSimple(n):

    if (n < 2):
        return False

    i = 2

    while (i <= n/2):
        if (n % i == 0):
            return False

        i += 1
    return True

divs = []

i = 2
while (n>1):
    if (isSimple(i) and ((n % i) == 0)):
        divs.append(i)
        n = n // i
    else:
        i += 1

print(divs)