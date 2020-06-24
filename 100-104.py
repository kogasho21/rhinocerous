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

domain = rs.CurveDomain(curve)
sections = []
dt = (domain[1] - domain[0]) / 10

for i in range(0, 10):
    t = domain[0] + i * dt
    points = []
    xyz = rs.EvaluateCurve(curve, t)
    R = xyz[0]
    z = xyz[2]
    dphi = 2 * ma.pi / 100
    for k in range(0, 101):
        phi = k * dphi
        x = (R + a*(ma.cos(n*phi) - 1)) * ma.cos(phi)
        y = (R + a*(ma.cos(n*phi) - 1)) * ma.sin(phi)
        points.append([x, y, z])
    sections.append(rs.AddInterpCurve(points))
top = rs.EvaluateCurve(curve, domain[1])
plane = rs.PlaneFromNormal(top, [0,0,1])
sections.append(rs.AddCircle(plane, 1))

rs.AddLayer("Cactus")
rs.CurrentLayer("Cactus")
surf = rs.AddLoftSrf(sections)
rs.CapPlanarHoles(surf)

cone = rs.AddCone([0,0,-sh], sh, sh)
basis = []
theta = ma.pi / 8
dphi = 2*ma.pi / m
for k in range(0, m):
    phi = k * dphi
    x = ma.sin(theta) * ma.cos(phi)
    y = ma.sin(theta) * ma.sin(phi)
    z = ma.cos(theta)
    matrix = rs.XformRotation3([0,0,1], [x,y,z], [0,0,0])
    basis.append(rs.TransformObject(cone, matrix, True))
rs.DeleteObject(cone)
