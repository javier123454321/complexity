import rhinoscriptsyntax as rs
import ghpythonlib as ghp

def fractalizeCurve(curve, numsteps, output_lines):
    numsteps -= 1  
    
    #Get endpoints from input curve
    curvePoints = rs.AddPoints(rs.CurvePoints(curve))
    pt0 = curvePoints[0]
    pt1 = curvePoints[1]
    
    #rotate input curve by input angle and form a triangle
    new_pt = rs.RotateObject(pt1, pt0, angle, axis=None, copy=True)
    
    new_line1 = rs.AddCurve([pt0, new_pt])
    new_line2 = rs.AddCurve([new_pt, pt1])
    
    #Append all the new lines into an input list
    output_lines.append(new_line1)
    output_lines.append(new_line2)
    
    #iterate the function as many times as requested
    if numsteps > 0:
        fractalizeCurve(new_line1, (numsteps), output_lines)
        fractalizeCurve(new_line2, (numsteps), output_lines)
    else:
        return output_lines        

a = []
fractalizeCurve(inputCrv, recursion_steps, a)

    
