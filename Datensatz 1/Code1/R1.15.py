temperatures = [
    0.00, 20.02, 20.14, 20.08, 19.91, 20.00, 20.24, 20.14, 20.14, 20.14, 
    20.15, 20.03, 20.10, 20.21, 20.24, 20.15, 20.33, 20.40, 20.13, 20.21, 
    20.33, 20.27, 20.43, 20.37, 20.53, 20.48, 20.32, 20.38, 20.51, 20.44, 
    20.37, 20.49, 20.52, 20.65, 20.73, 20.67, 20.72, 20.59, 20.70, 20.80, 
    20.70, 20.74, 21.09
]

sorted_temperatures = sorted(temperatures)

# Quartile
Q1 = sorted_temperatures[len(sorted_temperatures) // 4] #00.25
Q2 = sorted_temperatures[2 * len(sorted_temperatures) // 4] #00.50
Q3 = sorted_temperatures[3 * len(sorted_temperatures) // 4] #00.75

<<<<<<< HEAD
# Berechne Dezile
=======
# Dezile

D1 = sorted_temperatures[len(sorted_temperatures) // 10] #00.10
D2 = sorted_temperatures[2 * len(sorted_temperatures) // 10] #00.20
D3 = sorted_temperatures[3 * len(sorted_temperatures) // 10] #00.30
D4 = sorted_temperatures[4 * len(sorted_temperatures) // 10] #00.40
D5 = sorted_temperatures[5 * len(sorted_temperatures) // 10] #00.50
D6 = sorted_temperatures[6 * len(sorted_temperatures) // 10] #00.60
D7 = sorted_temperatures[7 * len(sorted_temperatures) // 10] #00.70
D8 = sorted_temperatures[8 * len(sorted_temperatures) // 10] #00.80
D9 = sorted_temperatures[9 * len(sorted_temperatures) // 10] #00.90 

<<<<<<< HEAD
# Gib die Ergebnisse aus
=======
>>>>>>> 9e337e81a4b7d876b1dfa2857d09508e85e96b18
print(f'Quartile:')
print(f'Q1: {Q1:.2f}')
print(f'Q2 (Median): {Q2:.2f}')
print(f'Q3: {Q3:.2f}\n')

print(f'Dezile:')
print(f'D1: {D1:.2f}')
print(f'D2: {D2:.2f}')
print(f'D3: {D3:.2f}')
print(f'D4: {D4:.2f}')
print(f'D5: {D5:.2f}')
print(f'D6: {D6:.2f}')
print(f'D7: {D7:.2f}')
print(f'D8: {D8:.2f}')
print(f'D9: {D9:.2f}')
