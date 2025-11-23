import math

# 1. Pobranie obwodu od użytkownika i konwersja na float
circumference = float(input('Enter tree circumference in cm: '))

# 2. Obliczenie średnicy (d = C / Pi)
diameter = circumference / math.pi  # POPRAWIONE: użyto math.pi

# 3. Sprawdzenie warunku i przypisanie wyniku logicznego (True/False)
# Ta linia zwraca True, jeśli diameter >= 50, w przeciwnym razie False
can_be_cut_down = diameter >= 50

# 4. Wyświetlenie wyniku zgodnie z formatem zadania
print(f"Tree can be cut down: {can_be_cut_down}")