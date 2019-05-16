import numpy as np
from enum import Enum
from collections import namedtuple
import random


class Env:

    DIM = 7
    INIT_STATE = np.array([
        [0, 0, 1, 1, 1, 0, 0], 
        [0, 0, 1, 1, 1, 0, 0], 
        [1, 1, 1, 1, 1, 1, 1], 
        [1, 1, 1, 0, 1, 1, 1], 
        [1, 1, 1, 1, 1, 1, 1], 
        [0, 0, 1, 1, 1, 0, 0],
        [0, 0, 1, 1, 1, 0, 0]])
    
    VALID_LOC_COUNT = (DIM*DIM)-(4*2*2)
    
    Action = namedtuple('Action', 'row col move')

    class Move(Enum):
        EAST = 0
        NORTH = 1
        WEST = 2
        SOUTH = 3
    
    pos2action = {
    
        (0, 2): [0, 1],
        (0, 3): [2],
        (0, 4): [3, 4],
    
        (1, 2): [5, 6],
        (1, 3): [7],
        (1, 4): [8, 9],
    
    
        (2, 0): [10, 11],
        (2, 1): [12, 13],
        (2, 2): [14, 15, 16, 17],
        (2, 3): [18, 19, 20, 21],
        (2, 4): [22, 23, 24, 25],
        (2, 5): [26, 27],
        (2, 6): [28, 29],


        (3, 0): [30],
        (3, 1): [31],
        (3, 2): [32, 33, 34, 35],
        (3, 3): [36, 37, 38, 39],
        (3, 4): [40, 41, 42, 43],
        (3, 5): [44],
        (3, 6): [45],


        (4, 0): [46, 47],
        (4, 1): [48, 49],
        (4, 2): [50, 51, 52, 53],
        (4, 3): [54, 55, 56, 57],
        (4, 4): [58, 59, 60, 61],
        (4, 5): [62, 63],
        (4, 6): [64, 65],


        (5, 2): [66, 67],
        (5, 3): [68],
        (5, 4): [69, 70],

        (6, 2): [71, 72],
        (6, 3): [73],
        (6, 4): [74, 75],
    
    }

    possible_actions = {
    
        0: Action(row=0, col=2, move=Move.EAST),
        1: Action(row=0, col=2, move=Move.SOUTH),
    
        2: Action(row=0, col=3, move=Move.SOUTH),
    
        3: Action(row=0, col=4, move=Move.WEST),
        4: Action(row=0, col=4, move=Move.SOUTH),
    
    
        5: Action(row=1, col=2, move=Move.EAST),
        6: Action(row=1, col=2, move=Move.SOUTH),

        7: Action(row=1, col=3, move=Move.SOUTH),

        8: Action(row=1, col=4, move=Move.WEST),
        9: Action(row=1, col=4, move=Move.SOUTH),


        10: Action(row=2, col=0, move=Move.EAST),
        11: Action(row=2, col=0, move=Move.SOUTH),

        12: Action(row=2, col=1, move=Move.EAST),
        13: Action(row=2, col=1, move=Move.SOUTH),

        14: Action(row=2, col=2, move=Move.EAST),
        15: Action(row=2, col=2, move=Move.NORTH),
        16: Action(row=2, col=2, move=Move.WEST),
        17: Action(row=2, col=2, move=Move.SOUTH),

        18: Action(row=2, col=3, move=Move.EAST),
        19: Action(row=2, col=3, move=Move.NORTH),
        20: Action(row=2, col=3, move=Move.WEST),
        21: Action(row=2, col=3, move=Move.SOUTH),

        22: Action(row=2, col=4, move=Move.EAST),
        23: Action(row=2, col=4, move=Move.NORTH),
        24: Action(row=2, col=4, move=Move.WEST),
        25: Action(row=2, col=4, move=Move.SOUTH),

        26: Action(row=2, col=5, move=Move.WEST),
        27: Action(row=2, col=5, move=Move.SOUTH),

        28: Action(row=2, col=6, move=Move.WEST),
        29: Action(row=2, col=6, move=Move.SOUTH),


        30: Action(row=3, col=0, move=Move.EAST),

        31: Action(row=3, col=1, move=Move.EAST),

        32: Action(row=3, col=2, move=Move.EAST),
        33: Action(row=3, col=2, move=Move.NORTH),
        34: Action(row=3, col=2, move=Move.WEST),
        35: Action(row=3, col=2, move=Move.SOUTH),

        36: Action(row=3, col=3, move=Move.EAST),
        37: Action(row=3, col=3, move=Move.NORTH),
        38: Action(row=3, col=3, move=Move.WEST),
        39: Action(row=3, col=3, move=Move.SOUTH),

        40: Action(row=3, col=4, move=Move.EAST),
        41: Action(row=3, col=4, move=Move.NORTH),
        42: Action(row=3, col=4, move=Move.WEST),
        43: Action(row=3, col=4, move=Move.SOUTH),

        44: Action(row=3, col=5, move=Move.WEST),

        45: Action(row=3, col=6, move=Move.WEST),


        46: Action(row=4, col=0, move=Move.EAST),
        47: Action(row=4, col=0, move=Move.NORTH),

        48: Action(row=4, col=1, move=Move.EAST),
        49: Action(row=4, col=1, move=Move.NORTH),

        50: Action(row=4, col=2, move=Move.EAST),
        51: Action(row=4, col=2, move=Move.SOUTH),
        52: Action(row=4, col=2, move=Move.SOUTH),
        53: Action(row=4, col=2, move=Move.EAST),

        54: Action(row=4, col=3, move=Move.EAST),
        55: Action(row=4, col=3, move=Move.NORTH),
        56: Action(row=4, col=3, move=Move.WEST),
        57: Action(row=4, col=3, move=Move.SOUTH),

        58: Action(row=4, col=4, move=Move.EAST),
        59: Action(row=4, col=4, move=Move.NORTH),
        60: Action(row=4, col=4, move=Move.WEST),
        61: Action(row=4, col=4, move=Move.SOUTH),

        62: Action(row=4, col=5, move=Move.NORTH),
        63: Action(row=4, col=5, move=Move.WEST),

        64: Action(row=4, col=6, move=Move.NORTH),
        65: Action(row=4, col=6, move=Move.WEST),


        66: Action(row=5, col=2, move=Move.EAST),
        67: Action(row=5, col=2, move=Move.NORTH),

        68: Action(row=5, col=3, move=Move.NORTH),

        69: Action(row=5, col=4, move=Move.NORTH),
        70: Action(row=5, col=4, move=Move.WEST),


        71: Action(row=6, col=2, move=Move.EAST),
        72: Action(row=6, col=2, move=Move.NORTH),

        73: Action(row=6, col=3, move=Move.NORTH),

        74: Action(row=6, col=4, move=Move.NORTH),
        75: Action(row=6, col=4, move=Move.WEST)

        }

    ACTION_N = len(possible_actions)

    def __init__(self):
        self.board = np.copy(Env.INIT_STATE)

    def set(self, board_state=INIT_STATE):
        self.board = np.copy(board_state)

    def reset(self):
        self.set()
        return self.board

    def boardify(self):

        self.board[0:2, 0:2] = 0
        self.board[5:7, 0:2] = 0
        self.board[0:2, 5:7] = 0
        self.board[5:7, 5:7] = 0

        if np.sum(self.board) == 33:
            self.board[3, 3] = 0

    def act(self, action):
        current = self.board[action.row][action.col]
        reward = 0
        if action.move == Env.Move.EAST:
            intermediate = self.board[action.row][action.col + 1]
            target = self.board[action.row][action.col + 2]
            if current == 1 and intermediate == 1 and target == 0:
                self.board[action.row][action.col] = 0
                self.board[action.row][action.col + 1] = 0
                self.board[action.row][action.col + 2] = 1
                reward = 1

        elif action.move == Env.Move.NORTH:
            intermediate = self.board[action.row - 1][action.col]
            target = self.board[action.row - 2][action.col]
            if current == 1 and intermediate == 1 and target == 0:
                self.board[action.row][action.col] = 0
                self.board[action.row - 1][action.col] = 0
                self.board[action.row - 2][action.col] = 1
                reward = 1

        elif action.move == Env.Move.WEST:
            intermediate = self.board[action.row][action.col - 1]
            target = self.board[action.row][action.col - 2]
            if current == 1 and intermediate == 1 and target == 0:
                self.board[action.row][action.col] = 0
                self.board[action.row][action.col - 1] = 0
                self.board[action.row][action.col - 2] = 1
                reward = 1

        elif action.move == Env.Move.SOUTH:
            intermediate = self.board[action.row + 1][action.col]
            target = self.board[action.row + 2][action.col]
            if current == 1 and intermediate == 1 and target == 0:
                self.board[action.row][action.col] = 0
                self.board[action.row + 1][action.col] = 0
                self.board[action.row + 2][action.col] = 1
                reward = 1

        return reward

    def valid_action(self, action):
        current = self.board[action.row][action.col]
        intermediate = self.board[action.row][action.col]
        target = self.board[action.row][action.col]

        if action.move == Env.Move.EAST:
            intermediate = self.board[action.row][action.col + 1]
            target = self.board[action.row][action.col + 2]

        elif action.move == Env.Move.NORTH:
            intermediate = self.board[action.row - 1][action.col]
            target = self.board[action.row - 2][action.col]

        elif action.move == Env.Move.WEST:
            intermediate = self.board[action.row][action.col - 1]
            target = self.board[action.row][action.col - 2]

        elif action.move == Env.Move.SOUTH:
            intermediate = self.board[action.row + 1][action.col]
            target = self.board[action.row + 2][action.col]

        if current == 1 and intermediate == 1 and target == 0:
            return True
        return False

    def get_count(self):
        return np.sum(self.board)

    def can_continue(self):
        a = np.nonzero(self.board)
        mapped = zip(a[0], a[1])
        mapped = set(mapped)

        for r, c in mapped:
            moves = Env.pos2action[(r, c)]
            for move in moves:
                if self.valid_action(Env.possible_actions[move]):
                    return True
        return False

    def get_state(self):
        return self.board

    def step(self, action_num):
        # act on action
        # get reward
        # do done check if required
        action = Env.possible_actions[action_num]
        done = False
        reward = self.act(action)

        if reward == 0:
            done = not(self.can_continue())

        if self.get_count() == 1:
            # game solved
            done = True

        return self.board, reward, done

    def sample_action(self):
        return random.randint(0, Env.ACTION_N-1)

    def sample_valid_action(self):
        action_num = self.sample_action()
        action = Env.possible_actions[action_num]
        while (not self.valid_action(action)) and self.can_continue():
            action_num = self.sample_action()
            action = Env.possible_actions[action_num]
        return action_num
