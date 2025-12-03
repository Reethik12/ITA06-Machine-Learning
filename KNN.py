from math import sqrt
from statistics import mode

data = [
    [30, 55, 1],     # test point
    [29, 60, 0],
    [32, 58, 0],
    [40, 70, 1],
    [25, 45, 0],
    [27, 48, 0],
    [35, 68, 1]
]

test = data[0]
data = data[1:]       

k = 3                

distances = []       
nearest_indices = []  
labels = []          

for row in data:
    dist = sqrt((row[0] - test[0])**2 + (row[1] - test[1])**2)
    distances.append(dist)

sorted_distances = sorted(distances)

for i in range(k):
    nearest_indices.append(distances.index(sorted_distances[i]))

for idx in nearest_indices:
    print(data[idx])
    labels.append(data[idx][-1])    

print("\nresult -->", mode(labels))