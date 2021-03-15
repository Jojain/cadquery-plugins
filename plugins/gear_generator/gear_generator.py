import cadquery as cq

class HollowCylinderSelector(cq.Selector):
    """
    Selects any shape present in the infinite hollow cylinder.   
    """
    #It works for the use I have in this code, it's not tested for any other configuration hence it might not be super robust
    def __init__(self, outer_radius, along_axis, height = None, inner_radius = None):
        self.r1 = inner_radius
        self.r2 = outer_radius
        self.axis = self.get_axis()


    def get_axis(axis_value):
        if along_axis == "X":
            self.axis = 0
        elif along_axis == "Y":
            self.axis = 1
        elif along_axis == "Z":
            self.axis = 2
        
    def filter(self, objectList):
        result =[]
        for o in objectList:
            p = o.Center()
            p_coords = [p.x, p.y, p.z]
            del p_coords[self.axis]
            p_radius = sqrt(p_coords[0]**2 + p_coords[1]**2)

            if p_radius> self.r1 and p_radius < self.r2 :   
                result.append(o)

        return result


def register():
    """
    Put the register function in order to be consistent with plugins initialization, even if it does nothing
    """

    pass
