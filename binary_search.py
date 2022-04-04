number_list = [42, 57, 12, 54, 23, 9, 17, 33]
number_list.sort()


def ask_for_user_input():
    user_input = input("Trage hier die gesuchte Nummer ein:")
    return user_input


def search_number():
    search = int(ask_for_user_input())
    if search in number_list:
        return print("Gesuchte Zahl gefunden")

    else:
        print("Die gesuchte Zahl ist nicht dabei.")
        ask_for_user_input()


search_number()

ask_for_user_input()
