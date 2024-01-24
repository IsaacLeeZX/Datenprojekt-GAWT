temperatures = [
    19.91, 20, 20.02, 20.03, 20.08, 20.1, 20.14, 20.14, 20.14, 
    20.14, 20.15, 20.15, 20.21, 20.21, 20.24, 20.24, 20.27, 20.32, 20.33, 
    20.33, 20.37, 20.37, 20.38, 20.4, 20.43, 20.44, 20.48, 20.49, 20.52, 20.53, 
    20.65, 20.67, 20.7, 20.73, 20.74, 20.8, 21.09
]

sorted_temperatures = sorted(temperatures)

# Quartile
Q1 = sorted_temperatures[len(sorted_temperatures) // 4]
Q3 = sorted_temperatures[3 * len(sorted_temperatures) // 4]

# Quartilsabstand
RQAbstand = Q3 - Q1 

print(f'Der Quartilsabstand R_Q0.5 beträgt: {RQAbstand:.2f}') 

# Quartilsabstand: 0.365