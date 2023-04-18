from geometry.parametric_geometry import ParametricGeometry


class PlaneGeometry(ParametricGeometry):

    def __init__(self, width=1, height=1, width_segments=8, height_segments=8):

        def S(u, v):
            return [u, v, 0]

        super().__init__(
            -width/2, width/2, width_segments,
            -height/2, height/2, height_segments,
            S)
