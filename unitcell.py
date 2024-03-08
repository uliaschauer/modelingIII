import numpy as np

class UnitCell:
    def __init__(self):
        self.cell_matrix = np.eye(3)
        self.atom_types = []
        self.atom_positions = [] # we store these as factional coordinates
        self.atom_charges = []

    def set_angle_lenths(self, a, b, c, alpha, beta, gamma):
        pass

    def set_vectors(self, ax, ay, az, bx, by, bz, cx, cy, cz):
        pass

    def add_atom_fractional(self, type, a, b, c, charge):
        self.atom_types.append(type)
        self.atom_positions.append(np.array([a, b, c]))
        self.atom_charges.append(charge)

    def add_atom_cartesian(self, type, x, y, z, charge):
        self.atom_types.append(type)
        self.atom_positions.append(self.cartesian_to_fractional(np.array([x, y, z])))
        self.atom_charges.append(charge)

    def cartesian_to_fractional(self, pos):
        pass

    def fractional_to_cartesian(self, pos):
        pass

    def fractional_coordinates(self):
        return self.atom_positions
    
    def cartesian_coordinates(self):
        pass

    def get_distance(self, i, j):
        pass
