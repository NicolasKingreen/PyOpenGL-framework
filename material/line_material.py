from material.basic_material import BasicMaterial
from OpenGL.GL import *


class LineMaterial(BasicMaterial):

    def __init__(self, properties={}):
        super().__init__()

        self.settings["drawStyle"] = GL_LINE_STRIP
        self.settings["lineWidth"] = 1
        self.settings["lineType"] = "connected"

        self.set_properties(properties)

    def update_render_settings(self):
        glLineWidth(self.settings["lineWidth"])
        if self.settings["lineType"] == "connected":
            self.settings["drawStyle"] = GL_LINE_STRIP
        elif self.settings["lineType"] == "loop":
            self.settings["drawStyle"] = GL_LINE_LOOP
        elif self.settings["lineType"] == "segments":
            self.settings["drawStyle"] = GL_LINES
        else:
            raise Exception("Unknown LineMaterial draw style.")
