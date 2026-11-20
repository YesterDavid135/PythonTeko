import random

CITIES = ["Basel", "Bern", "Zürich"]
DAYS = ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]


## A - Matrix mit Zufallswerten füllen
def fill_random(matrix):
    for row in range(3):          # 3 Städte
        for col in range(7):      # 7 Tage
            matrix[row][col] = round(random.uniform(-10, 35), 1)


## B - Durchschnitt einer Stadt
def average(matrix, city):
    total = 0
    for temp in matrix[city]:
        total = total + temp
    return round(total / 7, 1)


## C - Maximum einer Stadt
def maximum(matrix, city):
    highest = matrix[city][0]     # mit dem ersten Tag anfangen
    for temp in matrix[city]:
        if temp > highest:
            highest = temp
    return highest


## D - Matrix als Tabelle ausgeben
def print_matrix(matrix):
    # Kopfzeile mit den Wochentagen
    print(f"{'':8}", end="")
    for day in DAYS:
        print(f"{day:>7}", end="")
    print()

    # Eine Zeile pro Stadt
    for row in range(3):
        print(f"{CITIES[row]:8}", end="")
        for col in range(7):
            print(f"{matrix[row][col]:7}", end="")
        print()


## Zusatz - wärmster Tag über alle Städte gemittelt
def warmest_day(matrix):
    best_day = 0
    best_average = -100
    for col in range(7):
        total = 0
        for row in range(3):
            total = total + matrix[row][col]
        day_average = total / 3
        if day_average > best_average:
            best_average = day_average
            best_day = col
    return DAYS[best_day], round(best_average, 1)


## Hauptprogramm
temperatures = [[0 for x in range(7)] for y in range(3)]  # 3 Städte x 7 Tage
fill_random(temperatures)

print_matrix(temperatures)
print()

for city in range(3):
    print(CITIES[city], "- Durchschnitt:", average(temperatures, city),
          "°C, Maximum:", maximum(temperatures, city), "°C")
print()

day, temp = warmest_day(temperatures)
print("Wärmster Tag (Mittel aller Städte):", day, "mit", temp, "°C")
