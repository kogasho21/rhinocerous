import rhinoscriptsyntax as rs

Radius = 50
radius = 3.0
height = 100

rs.AddCone((0,0,0),height,Radius,True)
rs.AddCylinder((20,0,0),height,Radius,True)
rs.AddSphere((40,0,6),Radius)
rs.AddTorus((60,0,3),Radius,radius)
