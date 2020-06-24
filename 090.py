import rhinoscriptsyntax as rs

def ccx():
    curve1 = rs.GetObject("Select first curve", 4)
    curve2 = rs.GetObject("Select second curve", 4)
    intersection_list = rs.CurveCurveIntersection(curve1, curve2)
    if intersection_list is None:
        print "Selected curves do not intersect."
        return

    for intersection in intersection_list:
        print ("Point")
        print ("Intersection point on first curve:")
        print (intersection[1])
        print ("Intersection point on second curve:")
        print (intersection[3])
        print ("First curve parameter:")
        print (intersection[5])
        print ("Second curve parameter:")
        print (intersection[7])
ccx()
