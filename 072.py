import rhinoscriptsyntax as rs

objs = rs.GetObjects("Pick curves to loft" ,4)
rs.AddLoftSrf(objs, None, None, 1)
