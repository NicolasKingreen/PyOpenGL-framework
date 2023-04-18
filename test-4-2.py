from core.base import Base
from core.renderer import Renderer
from core.scene import Scene
from core.camera import Camera
from core.mesh import Mesh
from geometry.geometry import Geometry
from material.surface_material import SurfaceMaterial


class Test(Base):

    def initialize(self):
        print("Initializing program...")

        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera(aspect_ratio=800/600)
        self.camera.set_position([0, 0, 4])

        geometry = Geometry()
        P0 = [-0.1,  0.1, 0.0]
        P1 = [ 0.0,  0.0, 0.0]
        P2 = [ 0.1,  0.1, 0.0]
        P3 = [-0.2, -0.2, 0.0]
        P4 = [ 0.2, -0.2, 0.0]
        pos_data = [
            P0, P3, P1,
            P1, P3, P4,
            P1, P4, P2
        ]
        geometry.add_attribute("vec3", "vertexPosition", pos_data)
        R = [1, 0, 0]
        Y = [1, 1, 0]
        G = [0, 0.25, 0]
        color_data = [
            R, G, Y,
            Y, G, G,
            Y, G, R
        ]
        geometry.add_attribute("vec3", "vertexColor", color_data)
        geometry.count_vertices()

        material = SurfaceMaterial({
            "useVertexColors": True,
            # "wireframe": True
        })
        self.mesh = Mesh(geometry, material)
        self.mesh.scale(8)
        self.scene.add(self.mesh)

    def update(self):
        # self.mesh.rotate_y(0.0514)
        # self.mesh.rotate_x(0.0337)
        self.renderer.render(self.scene, self.camera)


if __name__ == "__main__":
    Test(screen_size=[800, 600]).run()
