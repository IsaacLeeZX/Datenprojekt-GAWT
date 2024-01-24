import matplotlib.pyplot as plt

jahre = [1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,2000,2001,2002,2003,2004,2005,2006,2007,2008,2010,2011,2012,2013,2014,2015,2016,2020,2021,2022,2023
]
temperaturen = [20.02,20.14,20.08,19.91,20,20.24,20.14,20.14,20.14,20.15,20.03,20.1,20.21,20.24,20.15,20.33,20.4,20.21,20.33,20.27,20.43,20.37,20.53,20.48,20.32,20.38,20.44,20.37,20.49,20.52,20.65,20.73,20.67,20.8,20.7,20.74,21.09
]

plt.figure(figsize=(10, 6))
plt.scatter(jahre, temperaturen, color='blue', marker='o')
plt.title('Scatterplot der Temperatur über die Jahre')
plt.xlabel('Jahr')
plt.ylabel('Temperatur (°C)')
plt.grid(True)
plt.show()
