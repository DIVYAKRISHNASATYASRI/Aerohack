import numpy as np
import pickle

def generate_phase1_table():
    # Precompute pruning table
    table = np.zeros(88179, dtype=np.uint8)
    # ... computation logic ...
    np.save('data/phase1.npy', table)
