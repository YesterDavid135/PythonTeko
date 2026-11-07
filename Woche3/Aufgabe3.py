MWST_SATZ = 1.081 # 8.1 % in CH
RABATTIERTE_KUNDENGRUPPE = 10 # Kunden mit einer Kundengruppe über 10 erhalten einen Rabatt
RABATT_FAKTOR = 0.95

def berechne_endpreis(einzelpreis, anzahl, kundengruppe):
    """Berechnet den endpreis des einkaufs.
        Parameter:
            einzelpreis: einzelpreis des Artikels
            anzahl: Anzahl der Artikel
            kundengruppe: Kundengruppe, des Kunden. Ab Gruppe 10 gibt es einen Rabatt.
        Rückgabe:
            Berechneter Endpreis
"""
    a= einzelpreis * anzahl
    if kundengruppe>= RABATTIERTE_KUNDENGRUPPE:
        a=a * RABATT_FAKTOR
    return a * MWST_SATZ

total=berechne_endpreis(11,10,11)
print(round(total,2) , "CHF")
