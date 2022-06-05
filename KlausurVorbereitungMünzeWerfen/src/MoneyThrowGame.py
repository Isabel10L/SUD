# Münze hat zwei Seiten; Eingabe: wie viele Würfe man machen kann; Wiedergabe: Ergebnis pro Wurf; Stichwort: random
import random

# Spieleinführung + Nutzereingabe
print("Willkommen beim Münzwurf!")
print("Wie viele Würfe wollen Sie machen?")
user_input_throw = int(input("Tragen Sie dazu eine ganze Zahl ein: ")) + 1

# VARIABLEN DELKARATION
try_throw = 0
head = 0
number = 0

# Durchführung des Spiels (Spiellogik)
for throw_repeat in range(1, user_input_throw):
    result = random.randint(1, 2)
    if result == 1:
        head = head + 1
        try_throw = try_throw + 1
        print(str(try_throw) + ": Kopf")
    else:
        number = number + 1
        try_throw = try_throw + 1
        print(str(try_throw) + ": Zahl")


# Spielauswertung
def winner_result(count_head, count_number):
    print("Anzahl des Ergebnisses 'Kopf': " + str(count_head))
    print("Anzahl des Ergebnisses 'Zahl': " + str(count_number))
    if count_head > count_number:
        print("Kopf hat gewonnen!")
    elif count_head < count_number:
        print("Zahl hat gewonnen!")
    else:
        print("Es ist gleichstand.")


winner_result(head, number)
