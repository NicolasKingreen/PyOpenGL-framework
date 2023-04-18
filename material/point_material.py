from material.basic_material import BasicMaterial
from OpenGL.GL import *


class PointMaterial(BasicMaterial):

    def __init__(self, properties={}):
        super().__init__()

        self.settings["drawStyle"] = GL_POINTS
        self.settings["pointSize"] = 8
        self.settings["roundedPoints"] = False

        self.set_properties(properties)

    def update_render_settings(self):

        glPointSize(self.settings["pointSize"])

        # doesn't work on macOS
        # if self.settings["roundedPoints"]:
        #     glEnable(GL_POINT_SMOOTH)
        # else:
        #     glDisable(GL_POINT_SMOOTH)

