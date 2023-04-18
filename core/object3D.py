from core.matrix import Matrix


class Object3D:

    def __init__(self):
        self.transform = Matrix.make_identity()
        self.parent = None
        self.children = []

    def add(self, child):
        self.children.append(child)
        child.parent = self

    def remove(self, child):
        self.children.remove(child)
        child.parent = None

    def get_world_matrix(self):
        if self.parent is None:
            return self.transform
        else:
            return self.parent.get_world_matrix() @ self.transform

    def get_descendant_list(self):
        descendants = []
        nodes_to_process = [self]
        while len(nodes_to_process) > 0:
            node = nodes_to_process.pop(0)
            descendants.append(node)
            nodes_to_process = node.children + nodes_to_process  # goes deeper
        return descendants

    def apply_matrix(self, matrix, local_coord=True):
        if local_coord:
            self.transform = self.transform @ matrix
        else:
            self.transform = matrix @ self.transform

    def translate(self, x, y, z, local_coord=True):
        m = Matrix.make_translation(x, y, z)
        self.apply_matrix(m, local_coord)

    def rotate_x(self, angle, local_coord=True):
        m = Matrix.make_rotation_x(angle)
        self.apply_matrix(m, local_coord)

    def rotate_y(self, angle, local_coord=True):
        m = Matrix.make_rotation_y(angle)
        self.apply_matrix(m, local_coord)

    def rotate_z(self, angle, local_coord=True):
        m = Matrix.make_rotation_z(angle)
        self.apply_matrix(m, local_coord)

    def scale(self, s, local_coord=True):
        m = Matrix.make_scale(s)
        self.apply_matrix(m, local_coord)

    def get_position(self):
        return [
            self.transform.item((0, 3)),
            self.transform.item((1, 3)),
            self.transform.item((2, 3))
        ]

    def get_world_position(self):
        world_transform = self.get_world_matrix()
        return [
            world_transform.item((0, 3)),
            world_transform.item((1, 3)),
            world_transform.item((2, 3))
        ]

    def set_position(self, position):
        self.transform.itemset((0, 3), position[0])
        self.transform.itemset((1, 3), position[1])
        self.transform.itemset((2, 3), position[2])

