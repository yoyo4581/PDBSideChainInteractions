from coordinateExtract import Coordinate_Extract
import numpy as np
import plotly.express as px
import plotly

maximum_dist = int(input("Enter the maximum distance you wish to filter for Cation-Pi: "))
sPi = Coordinate_Extract(input("Enter the pdb file path location/ name if in same project: "))
distance_Matrix = sPi.define_Dist(maximum_dist)

Search = ['ARG', 'LYS']
Target = ['TYR','PHE','TRP','HIS']

num_Matrix = sPi.define_num(Search, Target)
select = sPi.AA_select
target = sPi.AA_target

newMatrix = np.zeros((350,350))


print(select)
print(target)
print(distance_Matrix.size)


for s in select:
    s_val = distance_Matrix[s]
    for p in target:
        print(s_val[p])
        newMatrix[s][p] = s_val[p]

count_outer = 0

for s in select:
    nonzeroVal = np.nonzero(newMatrix[s])
    if nonzeroVal[0].size !=0:
        minVal = np.min(newMatrix[s][np.nonzero(newMatrix[s])])
        count_inner = 0
        for i in range(350):
            if newMatrix[s][i]==minVal:
                print(sPi.AA_names[s], s+1, sPi.AA_names[i], i+1, distance_Matrix[s][i])
        count_outer = count_outer + 1

