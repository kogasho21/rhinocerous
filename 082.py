import rhinoscriptsyntax as rs

base_point = ( 20, 10, 5)
vector_A = ( 10, 10, 10)

rs.AddPoint(base_point)
tip_point = rs.PointAdd(base_point, vector_A)
line = rs.AddLine(base_point, tip_point)
rs.CurveArrows(line, 2)
