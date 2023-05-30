# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

import random
x = random.randint(0, 999)
y = random.randint(0, 999)
s = x + y
p = x * y
# print(x, y)
print("The sum of numbers is:", s)
print("The multiplication of numbers is:", p)

xk=0
yk=0
match_found = False

while xk < 1000:
    while yk < 1000:
        if xk+yk == s and xk*yk == p:
            print("Numbers are", xk, yk)
            match_found = True
            break
        yk +=1
    if match_found:
        break
    yk = 0
    xk +=1
