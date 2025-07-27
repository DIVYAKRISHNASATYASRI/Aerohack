from numba import njit
import numpy as np

class KociembaSolver:
    def __init__(self):
        self.phase1_db = np.load('data/phase1.npy')
        self.phase2_db = np.load('data/phase2.npy')

    @njit
    def _phase1(self, cube_state):
        # Implement IDDFS with pruning
        pass

    def solve(self, cube):
        return self._phase1(cube.state) + self._phase2(cube.state)
