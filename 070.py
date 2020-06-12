import rhinoscriptsyntax as rs
import math as ma

count = 51,51
points = []
for i in range(count[0]):
    for j in range(count[1]):
        x = i*1.5
        y = j*1.5
        z = 5*ma.sin(i*ma.pi/24)*ma.cos(j*ma.pi/24)
        pt = x,y,z
        points.append(pt)
rs.AddSrfPtGrid(count,points)
