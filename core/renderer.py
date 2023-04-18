from OpenGL.GL import *
from core.mesh import Mesh


class Renderer:

    def __init__(self, clear_color=[0, 0, 0]):

        glEnable(GL_DEPTH_TEST)
        glEnable(GL_MULTISAMPLE)
        glClearColor(clear_color[0], clear_color[1], clear_color[2], 1)
        # glEnable(GL_BLEND)
        # glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    def render(self, scene, camera):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        camera.update_view_matrix()

        descendant_list = scene.get_descendant_list()
        mesh_filter = lambda x: isinstance(x, Mesh)
        mesh_list = list(filter(mesh_filter, descendant_list))

        for mesh in mesh_list:

            if not mesh.visible:
                continue

            glUseProgram(mesh.material.program_ref)

            glBindVertexArray(mesh.vao_ref)

            mesh.material.uniforms["modelMatrix"].data = mesh.get_world_matrix()
            mesh.material.uniforms["viewMatrix"].data = camera.view_matrix
            mesh.material.uniforms["projectionMatrix"].data = camera.projection_matrix

            for variable_name, uniform_object in mesh.material.uniforms.items():
                uniform_object.upload_data()

            mesh.material.update_render_settings()

            glDrawArrays(mesh.material.settings["drawStyle"], 0, mesh.geometry.vertex_count)
