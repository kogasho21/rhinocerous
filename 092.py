import rhinoscriptsyntax as rs

curveA = rs.GetObject("Select first curve", 4)
curveB = rs.GetObject("Select second curve", 4)
result = rs.CurveBooleanIntersection(curveA, curveB)


if result:
    rs.DeleteObject(curveA)
    rs.DeleteObject(curveB)
