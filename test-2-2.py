from core.base import Base
from core.openGLUtils import OpenGLUtils
from OpenGL.GL import *


class Test(Base):
    def initialize(self):
        print("Initializing program...")

        vs_code = """
        void main()
        {
            gl_Position = vec4(0.0, 0.0, 0.0, 1.0);
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

        vao_ref = glGenVertexArrays(1)
        glBindVertexArray(vao_ref)

        glClearColor(1.0, 1.0, 1.0, 1.0)
        glPointSize(10)

    def update(self):
        glClear(GL_COLOR_BUFFER_BIT)

        glUseProgram(self.program_ref)
        glDrawArrays(GL_POINTS, 0, 1)


Test().run()

