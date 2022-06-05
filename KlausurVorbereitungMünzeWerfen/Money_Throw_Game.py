# Münze hat zwei seiten
# Eingabe, wie viele würfe man machen kann
# Ergebnis pro Wurf in Konsole eingeben
# Stichwort: random
import random

print("Willkommen beim Münzwurf!")
print("")
throw = int(input("Wie viele Würfe wollen Sie machen?")) + 1
try_throw = 0

for throw_repeat in range(1, throw):

    result = random.randint(1, 2)
    if result == 1:
        try_throw= try_throw +1
        print(str(try_throw) + ": Kopf")

    else:
        try_throw = try_throw + 1
        print(str(try_throw) + ": Zahl")
