import numpy as np

class Cube:
    def __init__(self):
        # Face order: U, D, F, B, L, R
        self.state = np.zeros((6,3,3), dtype=np.uint8)
        self._init_solved()
    
    def _init_solved(self):
        for i in range(6):
            self.state[i,:,:] = i  # Each face single color

    def apply_move(self, move: str):
        """Handles R, U', F2 etc."""
        face = {'R':5, 'U':0, 'F':2}[move[0]]
        rotations = 1 if "'" not in move else 3
        if '2' in move: rotations = 2
        self.state[face] = np.rot90(self.state[face], rotations)
