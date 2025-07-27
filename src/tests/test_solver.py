import unittest
import numpy as np
from pathlib import Path
from src.core.cube import Cube
from src.core.kociemba import KociembaSolver

class TestSolver(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Initialize solver with test databases
        cls.solver = KociembaSolver()
        cls.test_cases = [
            ("R U R' U'", 14),  # Known 14-move solution
            ("F R U B' L D2", 18)  # Expected 18-move solution
        ]

    def test_solution_length(self):
        """Verify solutions don't exceed 20 moves"""
        for scramble, expected_moves in self.test_cases:
            with self.subTest(scramble=scramble):
                cube = Cube().scramble(scramble)
                solution = self.solver.solve(cube)
                self.assertLessEqual(len(solution), 20)
                self.assertEqual(len(solution), expected_moves)

    def test_solution_correctness(self):
        """Verify solutions actually solve the cube"""
        cube = Cube().scramble("R U R' U'")
        solution = self.solver.solve(cube)
        for move in solution:
            cube.apply_move(move)
        self.assertTrue(cube.is_solved())

    def test_unsolvable_states(self):
        """Test invalid cube detection"""
        with self.assertRaises(ValueError):
            cube = Cube()
            # Create unsolvable state by swapping two edge pieces
            cube.state[0,0,1], cube.state[1,0,1] = cube.state[1,0,1], cube.state[0,0,1]
            self.solver.solve(cube)

if __name__ == "__main__":
    unittest.main()
