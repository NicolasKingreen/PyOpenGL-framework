from core.base import Base
from core.openGLUtils import OpenGLUtils
from core.attribute import Attribute
from OpenGL.GL import *


class Test(Base):

    def initialize(self):
        print("Initializing program...")
        # OpenGLUtils.print_system_info()

        vs_code = """
        in vec3 position;
        void main() 
        {
            gl_Position = vec4(position.x, position.y, position.z, 1.0);
        }
        """

        fs_code = """
        out vec4 fragColor;
        void main()
        {
            fragColor = vec4(1.0, 1.0, 0.0, 1.0);
        }
        """

        self.program_ref = OpenGLUtils.initialize_program(vs_code, fs_code)

        # glLineWidth(4.0)  # depricated
        vao_ref = glGenVertexArrays(1)
        glBindVertexArray(vao_ref)

        position_data = [
            [0.8, 0.0, 0.0],
            [0.4, 0.6, 0.0],
            [-0.4, 0.6, 0.0],
            [-0.8, 0.0, 0.0],
            [-0.4, -0.6, 0.0],
            [0.4, -0.6, 0.0]
        ]
        self.vertex_count = len(position_data)
        position_attribute = Attribute("vec3", position_data)
        position_attribute.associate_variable(self.program_ref, "position")

    def update(self):
        glUseProgram(self.program_ref)
        # can be used with GL_LINE_LOOP, GL_LINES, GL_LINE_STRIP; GL_TRIANGLES, GL_TRIANGLE_FAN
        glDrawArrays(GL_TRIANGLE_FAN, 0, self.vertex_count)


if __name__ == "__main__":
    Test().run()

