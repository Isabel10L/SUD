# Münze hat zwei seiten
# Eingabe, wie viele würfe man machen kann
# Ergebnis pro Wurf in Konsole eingeben
# Stichwort: random
import random

print("Willkommen beim Münzwurf!")
print("Wie viele Würfe wollen Sie machen?")
user_input_throw = int(input("Tragen Sie dazu eine ganze Zahl ein: ")) + 1
try_throw = 0
count_head = 0
count_number = 0

for throw_repeat in range(1, user_input_throw):
    result = random.randint(1, 2)
    if result == 1:
        count_head = count_head + 1
        try_throw = try_throw + 1
        print(str(try_throw) + ": Kopf")
    else:
        count_number = count_number + 1
        try_throw = try_throw + 1
        print(str(try_throw) + ": Zahl")

print("Anzahl des Ergebnisses 'Kopf': " + str(count_head))
print("Anzahl des Ergebnisses 'Zahl': " + str(count_number))

if count_head > count_number:
    print("Kopf hat gewonnen!")
elif count_head < count_number:
    print("Zahl hat gewonnen!")
else:
    print("Es ist gleichstand.")
