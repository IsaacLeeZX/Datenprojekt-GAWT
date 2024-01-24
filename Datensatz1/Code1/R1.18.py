import statistics

years = list(range(1982, 2024))

std_deviation = statistics.stdev(years)

print(f'Die Standardabweichung der Jahreszahlen ist: {std_deviation:.2f}')
#Rest manuell ausgerechnet
