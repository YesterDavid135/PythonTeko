anzahl_zeilen = 22 ##Input

counter = 1 ## Laufender Counter

for i in range(1, anzahl_zeilen + 1):
    for j in range(1, i+1):
        print(f"{counter:3}", end=' ') ## Aktuelle Zahl mit der Breite 3 ausgeben
        counter += 1
    i += 1
    print() ## Neue Zeile beginnen