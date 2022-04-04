# Palidrom-Aufgabe

print("Prüfen Sie ein Wort oder einen Satz ein Palidrom ist.")


def is_palidrom(test_name):
    if len(test_name) <= 1:
        return True

    last_letter = (len(test_name)) - 1

    if test_name[0] == test_name[last_letter]:
        return is_palidrom(test_name[1:(len(test_name) - 1)])


def ask_for_name():
    name = input("Trage hier das mögliche Palidrom ein: ")
    return name.lower()


def is_name(name):
    if is_palidrom(name):
        print(name.title() + " ist ein Palidrom")
    else:
        print(name.title() + " ist kein Palidrom")
        is_name(name=ask_for_name())


is_name(name=ask_for_name())
