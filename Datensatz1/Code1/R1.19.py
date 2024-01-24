import matplotlib.pyplot as plt

temperatures = [
    0.00, 20.02, 20.14, 20.08, 19.91, 20.00, 20.24, 20.14, 20.14, 20.14, 
    20.15, 20.03, 20.10, 20.21, 20.24, 20.15, 20.33, 20.40, 20.13, 20.21, 
    20.33, 20.27, 20.43, 20.37, 20.53, 20.48, 20.32, 20.38, 20.51, 20.44, 
    20.37, 20.49, 20.52, 20.65, 20.73, 20.67, 20.72, 20.59, 20.70, 20.80, 
    20.70, 20.74, 21.09
]

class_intervals = [19.8, 20, 20.2, 20.4, 20.6, 20.8, 21, 21.2]

class_assignments = [sum(1 for temp in temperatures if interval[0] <= temp < interval[1]) for interval in zip(class_intervals, class_intervals[1:])]

total_data_points = len(temperatures)

relative_frequencies = [count / total_data_points for count in class_assignments]

fig, ax1 = plt.subplots()
ax1.bar(range(1, len(class_intervals)), class_assignments, width=0.4, align='edge',alpha=0.5, label='Absolute Häufigkeit')
ax1.set_xlabel('Klassen: "a <= Temperatur x < b"')

ax2 = ax1.twinx()
ax2.bar(range(1, len(class_intervals)), relative_frequencies, width=0.4, align='edge', alpha=0.5, label='Relative Häufigkeit')

plt.xticks(range(1, len(class_intervals)), [f'Klasse {i}:\n [{class_intervals[i-1]}, {class_intervals[i]}[' for i in range(1, len(class_intervals))])
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
plt.title('Histogramm der Temperaturen mit relativen und absoluten Häufigkeiten')
plt.show()
