userInputFactorialNumber = int(input("Tragen Sie eine natürliche Zahl für die gewünschte Fakultät ein:"))
print(f"Die gewünscht natürliche Zahl lautet: {userInputFactorialNumber}")

factor = 1

for index in range(1, userInputFactorialNumber + 1):
    factor *= index
print(f'{userInputFactorialNumber}! = {factor}')
