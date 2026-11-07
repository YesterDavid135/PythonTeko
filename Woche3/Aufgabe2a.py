# Eingabe
a = float(input("Kantenlänge des Würfels in cm: "))

# Verarbeitung
volume = a ** 3
surface_area = 6 * (a ** 2)

# Ausgabe
print(f"Volumen: {volume:.2f} cm³")
print(f"Oberfläche: {surface_area:.2f} cm²")