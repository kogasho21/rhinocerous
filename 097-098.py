import rhinoscriptsyntax as rs
import math as ma

n = 12
a = 4
m = 6
sh = 10
sr = 0.5

curve = rs.GetObject("Select a curve", 4)

ridges = []
dphi = 360.0 / n
for k in range(0, n):
    phi = k * dphi
    xform = rs.XformRotation2(phi, [0,0,1], [0,0,0])
    ridges.append(rs.TransformObject(curve, xform, True))
