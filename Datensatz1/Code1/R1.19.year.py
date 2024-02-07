import matplotlib.pyplot as plt

years = list(range(1982, 2024))

class_intervals = [1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025]

class_assignments = [sum(1 for year in years if interval[0] <= year < interval[1]) for interval in zip(class_intervals, class_intervals[1:])]

total_data_points = len(years)

relative_frequencies = [count / total_data_points for count in class_assignments]

fig, ax1 = plt.subplots()
ax1.bar(range(1, len(class_intervals)), class_assignments, width=0.4, align='edge', alpha=0.5, label='Absolute Häufigkeit')
ax1.set_xlabel('Klassen: "a <= Jahr x < b"')

ax2 = ax1.twinx()
ax2.bar(range(1, len(class_intervals)), relative_frequencies, width=0.4, align='edge', alpha=0.5, label='Relative Häufigkeit')

plt.xticks(range(1, len(class_intervals)), [f'Klasse {i}:\n [{class_intervals[i-1]}, {class_intervals[i]}[' for i in range(1, len(class_intervals))])
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
plt.title('Histogramm der Jahre mit relativen und absoluten Häufigkeiten')
plt.show()
