# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

def min_flips(coins):
    count_heads = 0
    count_tails = 0

    for coin in coins:
        if coin == "H":
            count_heads += 1
        elif coin == "T":
            count_tails += 1

    min_flips = min(count_heads, count_tails)

    return min_flips

coins = ["H", "T", "T", "H", "H", "T", "T"]
minimum_flips = min_flips(coins)
print("The minimum number of coins to flip is:", minimum_flips)