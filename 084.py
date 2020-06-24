import rhinoscriptsyntax as rs

#Function to draw a vector_A
def AddVector(base, vec):
    rs.AddPoint(base)
    tip = rs.PointAdd(base, vec)
    line = rs.AddLine(base, tip)
    rs.CurveArrows(line, 2)

#Base_point and direction of an original vector
base_point = (20, 10 ,5)
vector_A = (10, 10 ,10)
AddVector(base_point, vector_A)

#Create vector
vector_B = rs.VectorCreate((25, 16, -2), base_point)
AddVector(base_point, vector_B)

#Vector add
vector_C = rs.VectorAdd(vector_A, vector_B)
AddVector(base_point, vector_C)

#vector dot product
s = rs.VectorDotProduct(vector_A, vector_B)
print s

#Vector cross product
vector_D = rs.VectorCrossProduct(vector_A, vector_B)
AddVector(base_point, vector_D)
length_D = rs.VectorLength(vector_D)
print length_D
