from coordinateExtract import Coordinate_Extract
import numpy as np
import plotly.express as px
import plotly

maximum_dist = int(input("Enter the maximum distance you wish to filter for Cation-Anion: "))
sPi = Coordinate_Extract(input("Enter the pdb file path location/ name if in same project: "))
distance_Matrix = sPi.define_Dist(maximum_dist)

Search = ['ARG', 'LYS']
Target = ['GLU','ASP']

num_Matrix = sPi.define_num(Search, Target)
Sulfur = sPi.AA_select
Pi = sPi.AA_target

newMatrix = np.zeros((350,350))


for s in Sulfur:
    s_val = distance_Matrix[s]
    for p in Pi:
        newMatrix[s][p] = s_val[p]

count_outer = 0
for s in Sulfur:
    nonzeroVal = np.nonzero(newMatrix[s])
    if nonzeroVal[0].size != 0:
        minVal = np.min(newMatrix[s][np.nonzero(newMatrix[s])])
        count_inner = 0
        for i in range(350):
            if newMatrix[s][i]==minVal:
                print(sPi.AA_names[s], s+1, sPi.AA_names[i], i+1, distance_Matrix[s][i])
        count_outer = count_outer + 1

