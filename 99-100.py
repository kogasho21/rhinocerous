import rhinoscriptsyntax as rs
import math as ma

points = []
R = 40
a = 4
n = 12
z = 0
dphi = 2 * ma.pi / 100
for k in range(0, 101):
    phi = k * dphi
    x = (R + a*(ma.cos(n*phi) - 1)) * ma.cos(phi)
    y = (R + a*(ma.cos(n*phi) - 1)) * ma.sin(phi)
    points.append([x , y, z])
rs.AddInterpCurve(points)
