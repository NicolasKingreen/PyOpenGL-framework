from geometry.geometry import Geometry


class ParametricGeometry(Geometry):

    def __init__(self,
                 u_start, u_end, u_resolution,
                 v_start, v_end, v_resolution,
                 surface_function):
        super().__init__()

        delta_u = (u_end - u_start) / u_resolution
        delta_v = (v_end - v_start) / v_resolution
        positions = []

        for u_index in range(u_resolution+1):
            v_array = []
            for v_index in range(v_resolution+1):
                u = u_start + u_index * delta_u
                v = v_start + v_index * delta_v
                v_array.append(surface_function(u, v))
            positions.append(v_array)

        position_data = []
        color_data = []

        C1, C2, C3 = [1, 0, 0], [0, 1, 0], [0, 0, 1]
        C4, C5, C6 = [0, 1, 1], [1, 0, 1], [1, 1, 0]

        for x_index in range(u_resolution):
            for y_index in range(v_resolution):
                pA = positions[x_index+0][y_index+0]
                pB = positions[x_index+1][y_index+0]
                pC = positions[x_index+0][y_index+1]
                pD = positions[x_index+1][y_index+1]
                position_data += [
                    pA.copy(), pB.copy(), pC.copy(),
                    pA.copy(), pC.copy(), pD.copy()
                ]
                color_data += [
                    C1, C2, C3,
                    C4, C5, C6
                ]

        self.add_attribute("vec3", "vertexPosition", position_data)
        self.add_attribute("vec3", "vertexColor", color_data)
        self.count_vertices()

