import rhinoscriptsyntax as rs

def AddVector(base, vec):
    rs.AddPoint(base)
    tip = rs.PointAdd(base, vec)
    line = rs.AddLine(base, tip)
    rs.CurveArrows(line, 2)

base_point = (20, 10 ,5)
vector_A = (10, 10 ,10)
AddVector(base_point, vector_A)

base_point = (0, 0, 0)
AddVector(base_point, vector_A)
