import GameLogik

class GameTest1:
    user_input: int

    def promt_user_input(self):
        self.user_input = int(input("Trage hier die Anzahl Würfe ein:"))

    def game_ausführen(self):
        myList = [""]

        i = 0
        while i <= self.user_input:
            i += 1
            GameLogik.logik_ausführen()
            myList.append(GameLogik)

        return myList

game = GameTest1()
game.promt_user_input()
print("Anzahl Würfe: ", game.game_ausführen())

