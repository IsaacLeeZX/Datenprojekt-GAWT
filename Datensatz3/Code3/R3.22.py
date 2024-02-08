temperatures = [
    19.91, 20, 20.02, 20.03, 20.08, 20.1, 20.14, 20.14, 20.14, 20.14, 
    20.15, 20.15, 20.21, 20.21, 20.24, 20.24, 20.27, 20.32, 20.33, 20.33, 
    20.37, 20.37, 20.38, 20.4, 20.43, 20.44, 20.48, 20.49, 20.52, 20.53, 
    20.65, 20.67, 20.7, 20.73, 20.74, 20.8, 21.09
]

years= [1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 
                   1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 2000, 
                   2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2010, 2011, 
                   2012, 2013, 2014, 2015, 2016, 2020, 2021, 2022, 2023
] 

# Mittelwert
mean_temperature = sum(temperatures) / len(temperatures)
mean_years = sum(years) / len(years)

# Kovarianz
covariance_xy = sum((x - mean_temperature) * (y - mean_years) for x, y in zip(temperatures, mean_years)) / (len(temperatures) - 1)

print(f'Die Kovarianz zwischen den Temperaturdaten und der zweiten Variable beträgt: {covariance_xy:.4f}')

# Kovarianz: 3.1006