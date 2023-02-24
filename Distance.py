import math

class Distance3D:
    def __init__(self, object, subject):
        self.object = object
        self.subject = subject

    def get_distance_list(self):
        if isinstance(self.object[0], float)==False:
            distance = list()
            for item in self.subject:
                AB = 100
                distance.append(AB)
        else:
            x0 = float(self.object[0])
            y0 = float(self.object[1])
            z0 = float(self.object[2])
            distance = list()
            for item in self.subject:
                if item=='Not applicable':
                    AB = 100
                    distance.append(AB)
                else:
                    x1 = item[0]
                    y1 = item[1]
                    z1 = item[2]
                    AB = math.sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2 + (z1 - z0) ** 2)
                    distance.append(AB)
        return distance

    def get_propensity_list(self):
        prop_list = list()
        for item in self.subject:
            prop_add = float(item) + float(self.object)
            prop_list.append(prop_add)
        return prop_list

class Midpoint3D:
    def __init__(self, object, subject):
        self.object = object
        self.subject = subject

    def get_midpoint(self):
        x0 = float(self.object[0])
        y0 = float(self.object[1])
        z0 = float(self.object[2])
        x1 = self.subject[0]
        y1 = self.subject[1]
        z1 = self.subject[2]
        midpoint = [((x1 + x0)/ 2) , ((y1 + y0)/ 2) , ((z1 - z0)/2)]
        return midpoint
