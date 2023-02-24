from Distance import Distance3D
import plotly.express as px
import re
import numpy as np

class Coordinate_Extract:
    def __init__(self, fileX):
        self.filepath = str(fileX)
        self.dictAAnum_coord = dict()
        self.AA_select = list()
        self.AA_target = list()
        self.AA_names = list()
        global comb_num
        comb_num = self.dictAAnum_coord.keys()

    def define_Dist(self, limit):
        global listOflist
        distMatrix = np.full((350,350), np.nan)

        count = 1
        for line in open(self.filepath):
            line = line.split()
            if line[0]=='ATOM':
                if len(line[7]) > 8:
                    error_coord = re.search(r'(.\d*.\d*)-(\d*.\d*)', line[7])
                    line[7] = error_coord.group(1)
                    line[8] = '-' + error_coord.group(2)
                if int(line[5])==count:
                    if line[3]=='MET':
                        if line[2]=='CE':
                            key = line[5]+line[3]
                            self.dictAAnum_coord[key]=float(line[6]), float(line[7]), float(line[8])
                            count = count+1
                    elif line[3]=='ASN':
                        if line[2]=='ND2':
                            key = line[5]+line[3]
                            self.dictAAnum_coord[key]=float(line[6]),float(line[7]),float(line[8])
                            count = count+1
                    elif line[3]=='ARG':
                        if line[2]=='NH2':
                            key = line[5]+line[3]
                            self.dictAAnum_coord[key]=float(line[6]),float(line[7]),float(line[8])
                            count = count+1
                    elif line[3]=='TYR':
                        if line[2]=='OH':
                            key = line[5]+line[3]
                            self.dictAAnum_coord[key]= float(line[6]), float(line[7]), float(line[8])
                            count = count+1
                    elif line[3]=='LEU':
                        if line[2]=='CD2':
                            key = line[5]+line[3]
                            self.dictAAnum_coord[key]=float(line[6]),float(line[7]),float(line[8])
                            count = count+1
                    elif line[3]=='GLY':
                        if line[2]=='CA':
                            key = line[5]+line[3]
                            self.dictAAnum_coord[key]=float(line[6]),float(line[7]),float(line[8])
                            count = count+1
                    elif line[3]=='ALA':
                        if line[2]=='CB':
                            key = line[5]+line[3]
                            self.dictAAnum_coord[key]=float(line[6]),float(line[7]),float(line[8])
                            count = count+1
                    elif line[3]=='CYS':
                        if line[2]=='SG':
                            key = line[5]+line[3]
                            self.dictAAnum_coord[key]=float(line[6]),float(line[7]),float(line[8])
                            count = count+1
                    elif line[3]=='ASP':
                        if line[2]=='OD2':
                            key = line[5]+line[3]
                            self.dictAAnum_coord[key]=float(line[6]),float(line[7]),float(line[8])
                            count = count+1
                    elif line[3]=='GLU':
                        if line[2]=='OE2':
                            key = line[5]+line[3]
                            self.dictAAnum_coord[key]=float(line[6]),float(line[7]),float(line[8])
                            count = count+1
                    elif line[3]=='PHE':
                        if line[2]=='CZ':
                            key = line[5]+line[3]
                            self.dictAAnum_coord[key]=float(line[6]),float(line[7]),float(line[8])
                            count = count+1
                    elif line[3]=='HIS':
                        if line[2]=='NE2':
                            key = line[5]+line[3]
                            self.dictAAnum_coord[key]=float(line[6]),float(line[7]),float(line[8])
                            count = count+1
                    elif line[3]=='ILE':
                        if line[2]=='CD1':
                            key = line[5]+line[3]
                            self.dictAAnum_coord[key]=float(line[6]),float(line[7]),float(line[8])
                            count = count+1
                    elif line[3]=='LYS':
                        if line[2]=='NZ':
                            key = line[5]+line[3]
                            self.dictAAnum_coord[key]=float(line[6]),float(line[7]),float(line[8])
                            count = count+1
                    elif line[3]=='PRO':
                        if line[2]=='CG':
                            key = line[5]+line[3]
                            self.dictAAnum_coord[key]=float(line[6]),float(line[7]),float(line[8])
                            count = count+1
                    elif line[3]=='GLN':
                        if line[2]=='NE2':
                            key = line[5]+line[3]
                            self.dictAAnum_coord[key]=float(line[6]),float(line[7]),float(line[8])
                            count = count+1
                    elif line[3]=='SER':
                        if line[2]=='OG':
                            key = line[5]+line[3]
                            self.dictAAnum_coord[key]=float(line[6]),float(line[7]),float(line[8])
                            count = count+1
                    elif line[3]=='THR':
                        if line[2]=='OG1':
                            key = line[5]+line[3]
                            self.dictAAnum_coord[key]=float(line[6]),float(line[7]),float(line[8])
                            count = count+1
                    elif line[3]=='VAL':
                        if line[2]=='CG1':
                            key = line[5]+line[3]
                            self.dictAAnum_coord[key]=float(line[6]),float(line[7]),float(line[8])
                            count = count+1
                    elif line[3]=='TRP':
                        if line[2]=='CZ3':
                            key = line[5]+line[3]
                            self.dictAAnum_coord[key]=float(line[6]),float(line[7]),float(line[8])
                            count = count+1

        outer=0
        inner=0
        for item in self.dictAAnum_coord.items():
            list1 = Distance3D(item[1], self.dictAAnum_coord.values())
            listofDistance = list1.get_distance_list()
            for item2 in listofDistance:
                if item2 < limit:
                    distMatrix[outer][inner] = item2
                else:
                    distMatrix[outer][inner] = 0
                inner = inner +1
            inner=0
            outer = outer+1
        return distMatrix


    def define_num(self, search_char, target_char):
        for item in comb_num:
            number = re.search(r'\d*', item)
            AA = re.search(r'\D+', item)
            self.AA_names.append(AA.group())
            if AA.group() in search_char:
                self.AA_select.append(int(number.group())-1)
            if AA.group() in target_char:
                self.AA_target.append(int(number.group())-1)

