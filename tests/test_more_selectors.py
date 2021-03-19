import cadquery as cq
from more_selectors import (HollowCylinderSelector,
                                    InfiniteCylinderSelector,
                                    CylinderSelector,
                                    InfHollowCylinderSelector,
                                    SphereSelector,
                                    HollowSphereSelector)


                                    

def test_basic_operation():
    """
    Tests that the bare minimum functionality is working.
    """

    sampleplugin.register()

    result = cq.Workplane().rect(50, 50, forConstruction=True).vertices().make_cubes(10)

    assert(result.solids().size() == 4)
