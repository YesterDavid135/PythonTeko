import math

zahl = int(input("Bitte zu prüfende Primzahl eingeben: "))

if zahl < 2:
    print(f"{zahl} ist keine Primzahl.")
else:
    wurzel = math.isqrt(zahl)

    for i in range(2, wurzel + 1): ##Alle zahlen bis inklusive Wurzel prüfen
        if zahl % i == 0: ## Wenn Modulo = 0 ergibt, konnte es ohne rest geteilt werden
            print(f"{zahl} ist keine Primzahl (teilbar durch {i}).")
            break
    else:
        print(f"{zahl} ist eine Primzahl.")
