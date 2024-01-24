def median_absolute_deviation(data):
    median = sorted(data)[len(data) // 2] if len(data) % 2 != 0 else sum(sorted(data)[len(data) // 2 - 1:len(data) // 2 + 1]) / 2
    deviations = [abs(x - median) for x in data]
    mad = sum(deviations) / len(deviations)
    return mad

temperatures = [19.91, 20, 20.02, 20.03, 20.08, 20.1, 20.14, 
                20.14, 20.14, 20.14, 20.15, 20.15, 20.21, 20.21, 
                20.24, 20.24, 20.27, 20.32, 20.33, 20.33, 20.37, 
                20.37, 20.38, 20.4, 20.43, 20.44, 20.48, 20.49, 20.52, 
                20.53, 20.65, 20.67, 20.7, 20.73, 20.74, 20.8, 21.09
]

mad_result = median_absolute_deviation(temperatures)
print(f'Die mittlere Abweichung vom Median beträgt: {mad_result:.2f}')

# Die mittlere Abweichung vom Median beträgt: 0.21 