import random

zufallszahl = random.randint(1, 100)
versuche = 0
print("Eine Zufallszahl zwischen 1 und 100 wurde generiert. Versuche sie zu erraten.")

while True:
    user_input = input("Geben Sie eine Zahl ein: ")

    if user_input.isdigit() and 1 <= int(user_input) <= 100: ## Überprüfen ob es eine Gültige Eingabe ist
        zahl = int(user_input)
        versuche += 1

        if zahl == zufallszahl: ## Richtiger Guess
            print(f"Richtig! Du hast {versuche} Versuche gebraucht.")
            break
        elif zahl > zufallszahl: ## Zahl ist kleiner
            print("Falsch! Die gesuchte Zahl ist kleiner.")
        else: ## Zahl ist grösser
            print("Falsch! Die gesuchte Zahl ist grösser.")
    else:
        print("Ungültige Eingabe! Bitte gib eine ganze Zahl zwischen 1 und 100 ein.")