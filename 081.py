import rhinoscriptsyntax as rs

S = ( 20, 10, 5)
T = ( 3, 20, 15)

line = rs.AddLine(S, T)
rs.CurveArrows(line, 2)
