text = input("Geben Sie einen Text ein: ").strip()

## A
count = 0
for char in text:
    if char.lower() == "n":
        count += 1
print("Anzahl 'n' (Schleife):", count)

## Variante 2
print("Anzahl 'n' (count):", text.lower().count("n"))

## B
words = text.split()
print("Anzahl Wörter:", len(words))

## C
print("Längstes Wort:", max(words, key=len))

## D
vocals = "aeiouäöü"
vocal_count = 0
for char in text.lower():
    if char in vocals:
        vocal_count += 1
print("Anzahl Vokale:", vocal_count)

## E
print("Rückwärts:", text[::-1])
