import rhinoscriptsyntax as rs

def ccx():
    curve1 = rs.GetObject("Select first curve", 4)
    curve2 = rs.GetObject("Select second curve", 4)
    intersection_list = rs.CurveCurveIntersection(curve1, curve2)
    if intersection_list is None:
        print "Selected curves do not intersect."
        return

    for intersection in intersection_list:
        print "Point"
        print "Intersection point on first curve:",
               intersection[1]
        print "Intersection point on second curve:",
               intersection[3]
        print "First curve parameter:",
               intersection[5]
        print "Second curve parameter:",
               intersection[7]
ccx()
