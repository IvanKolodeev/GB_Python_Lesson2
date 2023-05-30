# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

n = input("Enter the maximum number")
if n.isdigit():
    n = int(n)
    s = 0
    i = 1
    while s <= n:
        s = 2 ** i
        if s <= n:
            print(s,end=", ")
        i += 1

else:
    print("Invalid input. Please enter a three-digit number.")