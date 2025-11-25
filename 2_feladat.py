"""
Olvassunk be billentyűzetről tizedes törteket (float), és tároljuk őket egy listában!
A bevitel végét a 0.0 jelzi.
Majd oldjuk meg a következő feladatokat!
Minden feladat előtt a program írja ki a feladat sorszámát!

1. Volt-e 5.5-nél nagyobb szám a listában?
2. Írjuk ki az első olyan szám indexét, ami negatív és egész (pl.: -2.0, -5.0)!
3. Hány darab 1 és 2 közé eső szám szerepel a listában?
4. Melyik volt a legnagyobb értékű negatív szám, és hányadik helyen állt?
5. Mennyi a pozitív számok összege?
"""

user_input = None
chosen_nums = []
while user_input != 0.0:
    try:
        user_input = float(input("Kérek tizedes törteket! (0-val jelezd, ha végeztél) "))
        chosen_nums.append(user_input)
    except ValueError as e:
        print("Kérlek tizedesvessző helyett pontot használj!")
        print(e)

# a 0.0 eltávolítása a lista végéről
chosen_nums.remove(0.0)

# 1. feladat
print("1. Volt-e 5.5-nél nagyobb szám a listában?")

try:
    for num in chosen_nums:
        if num > 5.5:
            print("Volt 5.5-nél nagyobb szám.")
            break
        else: 
            print("Nem volt ilyen szám.")
            break
except ValueError:
    print("Nem volt ilyen szám.")

# 2. feladat
print("2. Írjuk ki az első olyan szám indexét, ami negatív és egész (pl.: -2.0, -5.0)!")

for num in chosen_nums:
    if num < 0 and num % 1 == 0:
        first_int = num
        first_int_index = chosen_nums.index(first_int) + 1
        print(f"Az első negatív egész szám indexe: {first_int_index}. ")
        break
    else: 
        print("Nem volt ilyen szám.")


# 3. feladat
print("3. Hány darab 1 és 2 közé eső szám szerepel a listában?")

counter = 0
for num in chosen_nums:
    if 1.0 < num < 2.0:
        counter += 1
        print(f"Az adott intervallumban {counter} szám van.")
        break
    else: 
        print("Nem volt ilyen szám.")
        break


# 4. feladat
print("Melyik volt a legnagyobb értékű negatív szám, és hányadik helyen állt?")
try:
    #negatív számok kikeresése
    negatives = []
    for num in chosen_nums:
        if num < 0:
            negatives.append(num)
    # legkisebb keresése
    biggest_num = min(negatives)
    biggest_index = chosen_nums.index(biggest_num) + 1
    print(f"A legnagyobb értékű negatív szám: {biggest_num}, melynek indexe: {biggest_index}")
except ValueError: 
    print("Nem volt ilyen szám")

# 5. feladat
sum_of_positives = 0
print("5. Mennyi a pozitív számok összege?")
for num in chosen_nums:
    if num > 0:
        sum_of_positives += num
print(f"A pozitív számok összege: {sum_of_positives}")