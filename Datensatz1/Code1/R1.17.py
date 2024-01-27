temperatures = [
    20.02, 20.14, 20.08, 19.91, 20.00, 20.24, 20.14, 20.14, 20.14, 
    20.15, 20.03, 20.10, 20.21, 20.24, 20.15, 20.33, 20.40, 20.13, 20.21, 
    20.33, 20.27, 20.43, 20.37, 20.53, 20.48, 20.32, 20.38, 20.51, 20.44, 
    20.37, 20.49, 20.52, 20.65, 20.73, 20.67, 20.72, 20.59, 20.70, 20.80, 
    20.70, 20.74, 21.09
]

years = [1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 
1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 
2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 
2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 
2021, 2022, 2023] 

# Mittelwert
mean_temperature = sum(temperatures) / len(temperatures)
mean_years = sum(years) / len(years)

# Kovarianz
covariance_xy = sum((x - mean_temperature) * (y - mean_years) for x, y in zip(temperatures, years)) / (len(temperatures) - 1)

print(f'Die Kovarianz zwischen den Temperaturdaten und der zweiten Variable beträgt: {covariance_xy:.4f}')

# Kovarianz: 2.9872 