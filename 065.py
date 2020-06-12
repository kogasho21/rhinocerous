import rhinoscriptsyntax as rs

surf_id = rs.GetObject("Select a surface",8)
print surf_id

area = rs.SurfaceArea(surf_id)
domainU = rs.SurfaceDomain(surf_id, 0)
domainV = rs.SurfaceDomain(surf_id, 1)

print "area = ",area
print "domain of u-direction = ",domainU
print "domain of v-direction = ",domainV

uv = (domainU[1]-domainU[0])/2,(domainV[1]-domainV[0])/2
center = rs.SurfaceEvaluate(surf_id,uv,1)
normal = rs.SurfaceNormal(surf_id, uv)

print "xyz co-ordinate of center = ", center[0]
print "normal vector = ",normal
normal = rs.VectorUnitize(normal)
normal = rs.VectorScale(normal,5)
start = center[0]
end = rs.VectorAdd(start, normal)
rs.AddPoint(center[0])
rs.AddLine(start, end)
