reactiontime = [
    211, 220, 259, 218, 234, 198, 231, 193, 210, 206, 207, 
    187, 231, 279, 204, 187, 204, 215, 186, 187, 222, 189, 202, 195, 210, 
    272, 208, 219, 131, 186, 192, 192, 220, 190, 223, 208, 235, 261, 241, 
    211, 229, 214, 195, 198, 210, 194, 270, 197, 191, 203, 215, 200, 214, 
    198, 181, 189, 224, 203, 424, 203, 224, 193, 195, 203, 232, 233, 214, 
    202, 212, 204, 192, 188, 271, 201, 198, 230, 235, 201, 220, 202, 510, 
    239, 236, 181, 192, 239, 195, 186, 264, 202, 348, 379, 236, 201, 190, 
    198, 204, 232, 184, 169, 250, 208, 194, 182, 195, 230, 194, 190
]


n = len(reactiontime)

if n < 2:
    raise ValueError("Die Stichprobe sollte mindestens zwei Datenpunkte enthalten.")

mean = sum(reactiontime) / n
squared_deviations = [(x - mean) ** 2 for x in reactiontime]

sample_variance_result = sum(squared_deviations) / (n - 1)

print(f'Die Stichprobenvarianz beträgt: {sample_variance_result:.4f}')

#Stichprobenvarianz: 2206.6466
#Standardabweichung: 46.975