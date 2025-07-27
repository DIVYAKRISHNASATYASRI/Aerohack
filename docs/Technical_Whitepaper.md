# Kociemba's Two-Phase Algorithm Implementation

## Core Architecture
```mermaid
graph TD
    A[Scrambled Cube] --> B(Phase 1: Reduce to G1 Group)
    B --> C{Depth-Limited Search}
    C -->|≤12 moves| D[G1 State]
    D --> E(Phase 2: Solve with Half-Turns)
    E -->|≤6 moves| F[Solved Cube]
