import rhinoscriptsyntax as rs
import math as ma

surf = rs.GetObject("Select a surface",8)

n=50
domainU = rs.SurfaceDomain(surf,0)
domainV = rs.SurfaceDomain(surf,1)
du = (domainU[1] - domainU[0])/n
dv = (domainV[1] - domainV[0])/n

for u in rs.frange(domainU[0],domainU[1], du):
    for v in rs.frange(domainV[0], domainV[1], dv):
        xyz = rs.EvaluateSurface(surf, u, v)
        rs.AddPoint(xyz)
        normal = rs.SurfaceNormal(surf, (u,v))
        normal = rs.VectorUnitize(normal)
        normal = rs.VectorScale(normal, 5)
        start = xyz
        end = rs.VectorAdd(xyz, normal)
        rs.AddLine(start, end)
