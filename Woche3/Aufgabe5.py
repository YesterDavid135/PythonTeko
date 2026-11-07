def lies_zahl(frage, minimum, maximum):

    while True:
        eingabe = input(frage).strip()

        # Komma durch Punkt ersetzen
        bereinigt = eingabe.replace(",", ".")

        try:
            zahl = float(bereinigt)
        except ValueError:
            print(f"Fehler: '{eingabe}' ist keine gültige Zahl. Bitte wiederholen.")
            continue

        if minimum <= zahl <= maximum:
            return zahl
        else:
            print(f"Fehler: {zahl} liegt außerhalb des Bereichs [{minimum}, {maximum}].")

lies_zahl("Wie alt bist du?" ,0, 100)