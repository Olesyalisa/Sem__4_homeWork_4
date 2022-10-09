#Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.

lst = list(map(int, input("enter numbers (interval) = ").split()))
print(f"Old list = {lst}")
newLst = []
[newLst.append(i) for i in lst if i not in newLst]
print(newLst)