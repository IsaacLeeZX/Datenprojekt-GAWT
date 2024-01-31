
temperatures = [
    20.02, 20.14, 20.08, 19.91, 20, 20.24, 20.14, 20.14, 20.14, 20.15, 
    20.03, 20.1, 20.21, 20.24, 20.15, 20.33, 20.4, 20.21, 20.33, 20.27, 20.43, 
    20.37, 20.53, 20.48, 20.32, 20.38, 20.44, 20.37, 20.49, 20.52, 20.65, 20.73, 
    20.67, 20.8, 20.7, 20.74, 21.09
] 

years = [
    1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 
    1993, 1994, 1995, 1996, 1997, 1998, 2000, 2001, 2002, 2003, 2004, 2005, 
    2006, 2007, 2008, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2020, 2021, 
    2022, 2023
] 

n = len(temperatures)
j = len(years)

if n < 2:
    raise ValueError("Die Stichprobe sollte mindestens zwei Datenpunkte enthalten.")

mean = sum(temperatures) / n 
squared_deviations = [(x - mean) ** 2 for x in temperatures]

sample_variance_result = sum(squared_deviations) / (n - 1)

if j < 2:
    raise ValueError("Die Stichprobe sollte mindestens zwei Datenpunkte enthalten.")

mean = sum(years) / j
squared_deviations = [(x - mean) ** 2 for x in years]

sample_variance_result2 = sum(squared_deviations) / (j - 1)

print(f'Die Stichprobenvarianz beträgt: {sample_variance_result:.4f}')
print(f'Die Stichprobenvarianz beträgt (Jahr): {sample_variance_result2:.4f}')

# Jahreszahlen
# Stichprobenvarianz beträgt: 0.0686
# Standardabweichung: 0.2619 

# Temp. 
# Stichprobenvarianz beträgt: 0.0686
# Standardabweichung: 0.2619 