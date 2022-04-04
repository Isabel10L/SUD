# Ziel des Programms: Gesamt Fläche der Wohnung


userInputRoom = int(input("Tragen Sie die Anzahl Räume ein:"))
print(f"Anzahl Räume beträgt: {userInputRoom}")

areaRoomList = []

while len(areaRoomList) != userInputRoom:

    userInputWall = int(input("Tragen Sie die Anzahl der Wände für diesen Raum ein:"))
    print(f"Anzahl Wände des Raumes beträgt: {userInputWall}")

    if userInputWall == 4:
        userInputLengthWallOne = int(input("Tragen Sie die Länge von der ersten Wand ein:"))

        userInputLengthWallTow = int(input("Tragen Sie die Länge von der zweiten Wand ein:"))

        areaRoom = userInputLengthWallOne * userInputLengthWallTow
        areaRoomList.append(areaRoom)
        print(f"Die Fläche beträgt  {areaRoom}")

    elif userInputWall == 6:
        print("Teilen Sie den Raum so, dass Sie zwei Rechtecke erhalten")
        userInputLengthWallOne = int(
            input("Tragen Sie die Länge von der ersten Wand des optisch größern ersten Rechtecks ein:"))
        userInputLengthWallTow = int(
            input("Tragen Sie die Länge von der zweiten Wand optisch größern des ersten Rechtecks ein:"))
        userInputLengthWallThree = int(
            input("Tragen Sie die Länge von der ersten Wand des zweiten optisch kleineren Rechtecks ein:"))
        userInputLengthWallFour = int(
            input("Tragen Sie die Länge von der zweiten Wand des zweiten optisch kleineren Rechtecks ein:"))
        areaRoom = userInputLengthWallOne * userInputLengthWallTow - userInputLengthWallThree * userInputLengthWallFour
        areaRoomList.append(areaRoom)
        print(f"Fläche des Raumes beträgt:  {areaRoom}")


    else:
        print("Ungültige Wand angabe.")

finalAreaOfFlat = sum(areaRoomList)
print(f"Die Gesamtfläche der Wohnung beträgt: {finalAreaOfFlat}")
