import matplotlib.pyplot as plt


temperatures = [20.02,20.14,20.08,19.91,20,20.24,20.14,20.14,20.14,20.15,20.03,20.1,20.21,20.24,20.15,20.33,20.4,20.21,20.33,20.27,20.43,20.37,20.53,20.48,20.32,20.38,20.44,20.37,20.49,20.52,20.65,20.73,20.67,20.8,20.7,20.74,21.09
]

plt.boxplot([temperatures], vert=False)

plt.xlabel('Temperatur (°C)', fontsize=12)

plt.show()
