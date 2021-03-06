import rhinoscriptsyntax as rs
import math

function = "math.sin(x) * math.cos(y)"
domain = (-10.0, 10.0, -15.0, 15.0)
nx = 50
ny = 75

def createMesh():
    xstep = (domain[1] - domain[0]) / nx
    ystep = (domain[3] - domain[2]) / ny
    verts = []
    for i in range(nx+1):
        x = domain[0] + i*xstep
        for j in range(ny+1):
            y = domain[2] + j*ystep
            z = solveEquation(function, x, y)
            verts.append((x,y,z))
        faces = []
        for m in range(nx):
            for n in range(ny):
                e = m * (ny + 1) + n
                faces.append((e, e+1, e+ny+2, e+ny+1))
        rs.AddMesh(verts, faces)

def solveEquation(func, x, y):
    try:
        z = eval(func)
    except:
        z = 0
        return z

createMesh()
