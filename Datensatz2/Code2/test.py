temperatures = [
20.02, 20.14, 20.08, 19.91, 20.0, 20.24, 20.14, 20.14, 
20.14, 20.15, 20.03, 20.11, 20.21, 20.24, 20.15, 20.33, 20.41, 
20.21, 20.33, 20.27, 20.43, 20.37, 20.53, 20.48, 20.32, 
20.38, 20.44, 20.37, 

] 

n = len(temperatures)

if n < 2:
    raise ValueError("Die Stichprobe sollte mindestens zwei Datenpunkte enthalten.")

mean = sum(temperatures) / n
squared_deviations = [(x - mean) ** 2 for x in temperatures]

sample_variance_result = sum(squared_deviations) / (n - 1)

print(f'Die Stichprobenvarianz beträgt: {sample_variance_result:.4f}')

# Die Stichprobenvarianz beträgt: 0.0255 
# 2 * Standardabweichung = 0.3194