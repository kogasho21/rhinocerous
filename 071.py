import rhinoscriptsyntax as rs

curve = rs.GetObjects("Select curves",4)
axis = ((0, 0, 0),(0, 0, 1))
rs.AddRevSrf(curve, axis, 0, 360)
