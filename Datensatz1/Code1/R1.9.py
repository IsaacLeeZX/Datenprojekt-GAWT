def median_absolute_deviation(data):
    median = sorted(data)[len(data) // 2] if len(data) % 2 != 0 else sum(sorted(data)[len(data) // 2 - 1:len(data) // 2 + 1]) / 2
    deviations = [abs(x - median) for x in data]
    mad = sum(deviations) / len(deviations)
    return mad

temperatures = [20.02, 20.14, 20.08, 19.91, 20.10, 20.24, 20.14, 20.14, 20.14, 20.15, 20.03, 20.11, 20.21, 20.24, 20.15, 20.33, 20.41, 20.13, 20.21, 20.33, 20.27, 20.43, 20.37, 20.53, 20.48, 20.32, 20.38, 20.51, 20.44, 20.37, 20.49, 20.52, 20.65, 20.73, 20.67, 20.72, 20.59, 20.72, 20.82, 20.72, 20.74, 21.09]
years = [1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023.]
mad_result = median_absolute_deviation(temperatures)
mad_result2 = median_absolute_deviation(years)
print(f'Die mittlere Abweichung vom Median beträgt: {mad_result:.2f}')
print(f'Die mittlere Abweichung vom Median beträgt (Jahr): {mad_result2:.2f}')

# Die mittlere Abweichung vom Median beträgt (Jahr): 10.50
# Die mittlere Abweichung vom Median beträgt (Temp.): 0.21