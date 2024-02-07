Temperaturen = [
    0.00, 20.02, 20.14, 20.08, 19.91, 20.00, 20.24, 20.14, 20.14, 20.14, 
    20.15, 20.03, 20.10, 20.21, 20.24, 20.15, 20.33, 20.40, 20.13, 20.21, 
    20.33, 20.27, 20.43, 20.37, 20.53, 20.48, 20.32, 20.38, 20.51, 20.44, 
    20.37, 20.49, 20.52, 20.65, 20.73, 20.67, 20.72, 20.59, 20.70, 20.80, 
    20.70, 20.74, 21.09
]

Jahren  = list(range(1981, 2023))

mean_Temperaturen = sum(Temperaturen) / len(Temperaturen)
mean_Jahren = sum(Jahren) / len(Jahren) 

Kovarianz= sum((x - mean_Temperaturen) * (y - mean_Jahren) for x, y in zip(Temperaturen, Jahren)) / (len(Temperaturen) - 1)

print(f'Die Kovarianz zwischen den Temperaturdaten und den Jahreszahlen beträgt: {Kovarianz:.4f}') 
