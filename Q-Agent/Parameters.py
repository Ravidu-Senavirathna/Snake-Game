import sys
import os
import random

# ── point your sys.path at the folder containing your game files ─────────────
GAME_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../game"))
sys.path.insert(0, GAME_DIR)

import Constants


# ── Constants ───────────────────────────────────────────────────────────────
GRID_SIZE = 20          # 20×20 grid  →  each cell ≈ 40×30 px on an 800×600 screen

CELL_W = Constants.SCREEN_WIDTH  // GRID_SIZE
CELL_H = Constants.SCREEN_HEIGHT // GRID_SIZE





# ── Q-Learning Parameters ────────────────────────────────────────────────────
'''
Q-Learning is a model-free reinforcement learning algorithm that learns the value of taking a specific action in a given state. 
The key parameters for Q-Learning include:'''

# ── action definitions ────────────────────────────────────────────────────────
ACTIONS = {
    0: (0, -Constants.PLAYER_SPEED),   # UP
    1: (0,  Constants.PLAYER_SPEED),   # DOWN
    2: (-Constants.PLAYER_SPEED, 0),   # LEFT
    3: ( Constants.PLAYER_SPEED, 0),   # RIGHT
}

NUM_ACTIONS = len(ACTIONS)

# ── rewards ───────────────────────────────────────────────────────────────────
REWARD_COLLECT   =  50.0
REWARD_STEP      =  -1.0   # small penalty to encourage speed
REWARD_BOUNDARY  =  -25.0   # hit the wall
MAX_STEPS        = 2000      # episode length cap


# ── training parameters ───────────────────────────────────────────────────────
FPS        = 30     # slow enough to watch; increase for faster playback
NUM_GAMES  = 5      # how many episodes to play visually


# ── config ────────────────────────────────────────────────────────────────────
NUM_EPISODES  = 30000
PRINT_EVERY   = 200    # print to console every N episodes
RENDER_EVERY  = 100     # show the window every N episodes (0 = always render)
RENDER_FPS    = 600    # frame rate only during rendered episodes