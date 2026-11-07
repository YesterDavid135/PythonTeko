import math

# Eingabe
r = float(input("Radius der Kugel in cm: "))

# Verarbeitung
volume = (4 / 3) * math.pi * (r ** 3)
surface_area = 4 * math.pi * (r ** 2)

# Ausgabe
print(f"Volumen: {volume:.2f} cm³")
print(f"Oberfläche: {surface_area:.2f} cm²")