import unittest
from core.cube import Cube

class TestCube(unittest.TestCase):
    def test_move_application(self):
        cube = Cube()
        cube.apply_move("R")
        self.assertEqual(cube.state[5,0,0], 5)
