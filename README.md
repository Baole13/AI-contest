# 🧠 Tetris AI Agent

## 📝 Overview
This project implements a **Tetris-playing AI agent** built on top of a custom Tetris environment.  
The agent uses a **heuristic evaluation function** optimized through **genetic algorithm weights** to determine the best sequence of moves.

The core logic resides in the `Agent.py` file, which simulates the Tetris game environment and decision-making process.

---

## 🎮 Features
- Complete **Tetris environment simulation** (board state, blocks, rotations, collision checking).
- **Seven standard Tetris pieces** supported: I, O, J, L, Z, S, and T.
- Heuristic-based **move evaluation** (using height, holes, block count, line clears, etc.).
- Multi-step **lookahead search** to plan optimal moves.
- Agent interface (`choose_action`) designed to plug directly into Tetris AI competitions or reinforcement learning frameworks.

---

## 🧩 Code Structure

### 1. Core Classes and Functions

#### `Tetris`
A simulation of the Tetris game logic:
- Handles board state, piece movement, rotation, dropping, and line clearing.
- Computes useful board metrics for heuristic evaluation.

Key methods:
- `move(action)` – executes an action (drop, rotate, move left/right).
- `clear()` – clears completed lines.
- `get_info_from_state()` – extracts game state features (height, holes, etc.).

#### `Agent`
Main AI decision-maker that:
- Receives the current observation (`obs`).
- Simulates future states using a heuristic scoring function.
- Selects the **best possible move** sequence.
- Outputs a single integer action for the environment.

#### Helper Functions
- `initialize(obss)` – preprocesses observation data into board, holding piece, and next pieces.
- `get_best_move()` – performs multi-step simulation to choose optimal moves.
- `get_rating_from_move()` – evaluates a simulated game state using the genetic weights.
- `check_collision()`, `depth_drop()`, `get_possible_move_lists()` – utility functions for movement and collision logic.

---

## ⚙️ How It Works

1. The agent reads the Tetris board state (`obs`).
2. It reconstructs the board and next pieces.
3. For each possible move sequence, it:
   - Simulates dropping and rotating the piece.
   - Scores the resulting board using a weighted heuristic.
4. Chooses the sequence with the **highest rating**.
5. Returns the first move from that sequence.

---

## 🧮 Heuristic Function

The agent uses a vector of weights (`self.gen`) to evaluate board states:

| Feature | Description | Weight Example |
|----------|--------------|----------------|
| Height Sum | Total height of all columns | -0.45 |
| Height Difference | Roughness of surface | -0.32 |
| Max Height | Highest column | -0.52 |
| Hole Count | Number of gaps | -1.43 |
| Deepest Unfilled | Lowest empty cell | -0.82 |
| Block Count | Total placed blocks | 1.85 |
| Column Holes | Columns with holes | -1.59 |
| Lines Cleared | Reward for clearing lines | +0.77 |
| Pit/Hole Ratio | Ratio of filled to empty space | +1.85 |

These weights were likely evolved via a **genetic algorithm** to maximize performance.

---

## 🚀 Usage

### Prerequisites
- Python 3.8+
- `numpy`

Install dependencies:
```bash
pip install numpy
