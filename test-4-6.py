from core.base import Base
from core.renderer import Renderer
from core.scene import Scene
from core.camera import Camera
from core.mesh import Mesh
from geometry.box_geometry import BoxGeometry
from material.surface_material import SurfaceMaterial
from extras.axes_helper import AxesHelper
from extras.grid_helper import GridHelper
from extras.movement_rig import MovementRig
from math import pi


class Test(Base):

    def initialize(self):
        print("Initializing program...")

        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera(aspect_ratio=800/600)
        # self.camera.set_position([0.5, 1, 5])
        self.rig = MovementRig()
        self.rig.add(self.camera)
        self.rig.set_position([0.5, 1, 5])
        self.scene.add(self.rig)

        axes = AxesHelper(axis_length=2)
        self.scene.add(axes)

        grid = GridHelper(size=20, grid_color=[1, 1, 1],
                          center_color=[1, 1, 0])
        grid.rotate_x(-pi/2)
        self.scene.add(grid)

        geometry = BoxGeometry()
        material = SurfaceMaterial({
            "useVertexColors": True,
            # "wireframe": True
        })
        self.mesh = Mesh(geometry, material)
        self.scene.add(self.mesh)

    def update(self):
        # self.mesh.rotate_y(0.0514)
        # self.mesh.rotate_x(0.0337)
        self.rig.update(self.input, self.delta_time)
        self.renderer.render(self.scene, self.camera)


if __name__ == "__main__":
    Test(screen_size=[800, 600]).run()
