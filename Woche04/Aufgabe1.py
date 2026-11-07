MWST_SATZ = 1.081

try:
    menge = int(input("Geben Sie die gewünschte Menge an Schreibblöcken ein: "))

    if menge <= 0:
        print("Fehler: Ungültige Menge. Bitte eine Zahl grösser als 0 eingeben.")
    elif menge < 10:
        stueckpreis = 1.60
    elif menge < 100:
        stueckpreis = 1.40
    else:
        stueckpreis = 1.20

    if menge > 0:
        gesamtpreis = menge * stueckpreis
        # Berechnen der beinhalteter MwSt
        mwst_betrag = gesamtpreis - (gesamtpreis / MWST_SATZ)

        print("\n--- Abrechnung ---")
        print(f"Menge:        {menge} Stück")
        print(f"Stückpreis:   {stueckpreis:.2f} CHF")
        print(f"Gesamtpreis:  {gesamtpreis:.2f} CHF")
        print(f"Davon MWST:   {mwst_betrag:.2f} CHF (8.1 %)")

except ValueError:
    print("Fehler: Bitte gib eine ganze Zahl ein.")