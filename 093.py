import rhinoscriptsyntax as rs

curve_ids = rs.GetObjects("Select curves to union",4)
if len(curve_ids)>1:
    result = rs.CurveBooleanUnion(curve_ids)
    if result: rs.DeleteObjects(curve_ids)
