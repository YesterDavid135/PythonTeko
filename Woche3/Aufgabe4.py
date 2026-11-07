# Artikeldaten (Bezeichnung, Menge, Stückpreis)
artikel_liste = [
    ("Paulaner Spezi", 2, 1.80),
    ("Zigaretten", 1, 8.50),
    ("Mineralwasser", 3, 2.70),
]

trennlinie = "-" * 40

print(trennlinie)
print("             KIOSK QUITTUNG             ")
print(trennlinie)
print(f"{'Artikel':<18}{'Menge':>5}{'Preis':>8}{'Total':>9}")
print(trennlinie)

# Schleife für Ausgabe und Total-Berechnung
gesamt_total = 0.0
for name, menge, preis in artikel_liste:
    zeilen_total = menge * preis
    gesamt_total += zeilen_total
    print(f"{name:<18}{menge:>5}{preis:>8.2f}{zeilen_total:>9.2f}")

print(trennlinie)

# Rundung auf 5 Rappen
gesamt_bar = round(gesamt_total * 20) / 20

# Enthaltene MWST (8.1 % aus dem Bruttobetrag)
MWST_SATZ = 1.081
mwst_betrag = gesamt_total - (gesamt_total / MWST_SATZ)

# Bezahlung und Rückgeld
gegeben = 50.00
rueckgeld = gegeben - gesamt_bar

print(f"{'Gesamtbetrag:':<28}{gesamt_bar:>12.2f}")
print(f"{'Enthaltene MWST (8.1 %):':<28}{mwst_betrag:>12.2f}")
print(trennlinie)

print(f"{'Gegeben (CHF):':<28}{gegeben:>12.2f}")
print(f"{'Rückgeld (CHF):':<28}{rueckgeld:>12.2f}")
print(trennlinie)