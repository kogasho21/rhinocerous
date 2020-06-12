import rhinoscriptsyntax as rs

curves = rs.GetObjects("Select curves",4)
rs.AddEdgeSrf(curves)
