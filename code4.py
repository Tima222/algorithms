Дано натуральное число А (А<9999). Верно ли, что это число содержит ровно три одинаковые цифры, как, например, числа 6676, 4544 и тд

a=int(input())
a=str(a)
for i in str(a):
    if a.count(i)==3:
        print("Число содержит три одинаковые цифры")
        break
    else:
        continue
