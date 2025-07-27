import numpy as np
from numba import njit
import pickle
from pathlib import Path
from src.core.cube import Cube

# Phase 1: Corner orientation and permutation
@njit
def generate_phase1_table():
    table = np.full(88179, 255, dtype=np.uint8)  # 255 = unreachable
    table[0] = 0  # Solved state
    
    moves = ['U', 'U\'', 'U2', 'D', 'D\'', 'D2',
             'R2', 'L2', 'F2', 'B2']
    
    queue = [(0, 0)]  # (state, depth)
    
    while queue:
        state, depth = queue.pop(0)
        for move in moves:
            new_state = apply_move_phase1(state, move)
            if table[new_state] == 255:  # Unvisited
                table[new_state] = depth + 1
                queue.append((new_state, depth + 1))
    
    np.save('phase1.npy', table)

# Phase 2: Full cube solving
@njit 
def generate_phase2_table():
    table = np.full(42577920, 255, dtype=np.uint8)
    table[0] = 0
    
    moves = ['U', 'U\'', 'U2', 'D', 'D\'', 'D2',
             'R2', 'L2', 'F2', 'B2']
    
    queue = [(0, 0)]
    
    while queue:
        state, depth = queue.pop(0)
        for move in moves:
            new_state = apply_move_phase2(state, move)
            if table[new_state] == 255:
                table[new_state] = depth + 1
                if depth < 8:  # Phase 2 max depth
                    queue.append((new_state, depth + 1))
    
    np.save('phase2.npy', table)

if __name__ == "__main__":
    print("Generating phase1.npy...")
    generate_phase1_table()
    
    print("Generating phase2.npy...")
    generate_phase2_table()
    
    print("Pattern databases generated successfully")
