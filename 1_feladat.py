"""
Szimuláljuk egy 6 oldalú kocka 20 dobását! A dobásokat egy listában tároljuk!
Majd oldjuk meg a következő feladatokat!
Minden feladat előtt a program írja ki a feladat sorszámát!

1. Volt-e 5-ös dobás a listában?
2. Hanyadik dobás lett először 1-es?
3. Hány darab páros számot dobtunk?
4. Melyik volt a legkisebb dobás a 4-nél nagyobbak közül, és hányadik dobás volt?
5. Mennyi a 3-as dobások összege?

"""

import random as r

# a dobások szimulálása
drawn_nums = []
for i in range(20):
    dice = r.randint(1, 6)
    drawn_nums.append(dice)


print(f"Debug:\n{drawn_nums}")

# 1. feladat
print("1. Volt-e 5-ös dobás a listában?")

try:
    if 5 in drawn_nums:
        print(f"Igen, volt 5-ös dobás.")
except ValueError:
    print("Nem volt ilyen dobás.")

# 2. feladat
print("2. Hanyadik dobás lett először 1-es?")

try:
    print(f"Az első egyes dobás helye: {drawn_nums.index(1) + 1}")
except ValueError:
    print("Nem volt ilyen dobás.")

# 3. feladat
print("3. Hány darab páros számot dobtunk?")

try: 
    even_nums = []
    for even in drawn_nums:
        if even % 2 == 0:
            even_nums.append(even)

    print(f"Összesen {len(even_nums)} páros dobásunk volt.")    
except ValueError:
    print("Nem volt ilyen dobás.")


# 4. feladat
print("4. Melyik volt a legkisebb dobás a 4-nél nagyobbak közül, és hányadik dobás volt?")

try:
    # >4 számok kikeresése
    more_than_4 = []
    for greater_4 in drawn_nums:
        if greater_4 > 4:
            more_than_4.append(greater_4)

    # legkisebb keresése
    smallest_num = min(more_than_4)
    smallest_index = more_than_4.index(smallest_num) + 1

    print(f"A legkisebb dobás a 4 után: {smallest_num}, melynek helye: {smallest_index}")
except ValueError:
    print("Nem volt ilyen dobás")

# 5. feladat 
print("5. Mennyi a 3-as dobások összege?")

try:
    occurence_of_threes = drawn_nums.count(3)
    sum_of_threes = occurence_of_threes * 3

    print(f"A hármas dobások összege: {sum_of_threes}")
except ValueError:
    print("Nem volt ilyen dobás")