import random


class GameLogik:

    def logik_ausführen(self):
        ergebnis = random.randint(1, 2)

        if (ergebnis == 1):
            ergebnisValue = "Kopf"

        else:
            ergebnisValue = "Zahl"

        return ergebnisValue

logik = GameLogik