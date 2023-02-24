from coordinateExtract import Coordinate_Extract
import numpy as np
import plotly.express as px
import plotly

maximum_dist = int(input("Enter the maximum distance (A) you wish to filter for Pi-Pi (not 1 to 1): "))
sPi = Coordinate_Extract(input("Enter the pdb file path location/ name if in same project: "))
distance_Matrix = sPi.define_Dist(maximum_dist)

Search = ['TYR','PHE','TRP','HIS']
Target = ['TYR','PHE','TRP','HIS']

num_Matrix = sPi.define_num(Search, Target)
select = sPi.AA_select
target = sPi.AA_target

newMatrix = np.zeros((350,350))


for s in select:
    s_val = distance_Matrix[s]
    for p in target:
        newMatrix[s][p] = s_val[p]

count_outer = 0
for s in select:
    nonzeroVal = np.nonzero(newMatrix[s])
    if nonzeroVal[0].size != 0:
        for i in range(350):
            if newMatrix[s][i]!=0.0:
                print(sPi.AA_names[s], s+1, sPi.AA_names[i], i+1, distance_Matrix[s][i])
        count_outer = count_outer + 1

