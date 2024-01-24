import statistics

years = list(1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2020, 2021, 2022, 2023
)

std_deviation = statistics.stdev(years)

print(f'Die Standardabweichung der Jahreszahlen ist: {std_deviation:.2f}')
