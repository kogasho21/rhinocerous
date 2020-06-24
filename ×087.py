import rhinoscriptsyntax as rs

def AddVector(base, vec):
    tip = rs.PointAdd(base, vec)
    line = rs.AddLine(base, tip)
    rs.CurveArrows(line, 2)

curve = rs.GetObject("Select a curve" ,4)
domain = rs.CurveDomain(curve)

n=60
dt = (domain[1] - domain[0]) / n

for i in rs.frange(0, n, 1):
    t = i * dt
    xyz = rs.EvaluateCurve(curve, t)
    rs.AddPoint(xyz)
    tangent = rs.CurveTangent(curve, t)
    if tangent:
        x_axis = rs.VectorUnitize(tangent)
        tangent = rs.VectorScale(x_axis, 20)
        AddVector(xyz, tangent)
    normal = [-tangent[1], tangent[0], 0]
    if normal:
        y_axis = rs.VectorUnitize(normal)
        normal = rs.VectorScale(y_axis, 20)
        AddVector(xyz, normal)
    if tangent and normal:
        bi_normal = rs.VectorCrossProduct(x_axis, y_axis)
        z_axis = rs.VectorUnitize(bi_normal)
        bi_normal = rs.VectorScale(z_axis, 20)
        AddVector(xyz, bi_normal)
