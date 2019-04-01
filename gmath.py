import math
from display import *



#vector functions
#normalize vetor, should modify the parameter
def normalize(vector):
    factor=math.sqrt ( vector[0]**2 + vector[1]**2 + vector[2]**2 )
    vector[0]=vector[0]/factor
    vector[1]=vector[1]/factor
    vector[2]=vector[2]/factor

#Return the dot porduct of a . b
def dot_product(a, b):
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2]

#Calculate the surface normal for the triangle whose first
#point is located at index i in polygons
def calculate_normal(polygons, i):
    first=polygons[i]
    second=polygons[i+1]
    third=polygons[i+2]
    a = [first[0] - first[0],
         second[1] - first[1],
         second[2] - first[2]]
    b = [third[0] - second[0],
         third[1] - second[1],
         third[2] - second[2]]
    return [a[1]*b[2] - a[2]*b[1],
            a[2]*b[0] - a[0]*b[2],
            a[0]*b[1] - a[1]*b[0]]
