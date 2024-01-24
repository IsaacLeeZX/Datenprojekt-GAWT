temperatures = [
    0.00, 20.02, 20.14, 20.08, 19.91, 20.00, 20.24, 20.14, 20.14, 20.14, 
    20.15, 20.03, 20.10, 20.21, 20.24, 20.15, 20.33, 20.40, 20.13, 20.21, 
    20.33, 20.27, 20.43, 20.37, 20.53, 20.48, 20.32, 20.38, 20.51, 20.44, 
    20.37, 20.49, 20.52, 20.65, 20.73, 20.67, 20.72, 20.59, 20.70, 20.80, 
    20.70, 20.74, 21.09
]

# Sortiere die Daten
sorted_temperatures = sorted(temperatures)

# Berechne Quartile
Q1 = sorted_temperatures[len(sorted_temperatures) // 4]
Q3 = sorted_temperatures[3 * len(sorted_temperatures) // 4]

# Berechne Quartilsabstand
RQAbstand = Q3 - Q1 

# Gib das Ergebnis aus
print(f'Der Quartilsabstand R_Q0.5 beträgt: {RQAbstand:.2f}')
 