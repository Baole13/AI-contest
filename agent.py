import numpy as np
from copy import deepcopy
import random

DEFAULT_GRID = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
ipieces = [[[0, 0, 1, 0],
            [0, 0, 1, 0],
            [0, 0, 1, 0],
            [0, 0, 1, 0]],[[0, 0, 0, 0],
                           [0, 0, 0, 0],
                           [1, 1, 1, 1],
                           [0, 0, 0, 0]],[[0, 1, 0, 0],
                                          [0, 1, 0, 0],
                                          [0, 1, 0, 0],
                                          [0, 1, 0, 0]],[[0, 0, 0, 0],
                                                         [1, 1, 1, 1],
                                                         [0, 0, 0, 0],
                                                         [0, 0, 0, 0]]]
opieces = [[[0, 0, 0, 0],
            [0, 1, 1, 0],
            [0, 1, 1, 0],
            [0, 0, 0, 0]],[[0, 0, 0, 0],
                           [0, 1, 1, 0],
                           [0, 1, 1, 0],
                           [0, 0, 0, 0]],[[0, 0, 0, 0],
                                          [0, 1, 1, 0],
                                          [0, 1, 1, 0],
                                          [0, 0, 0, 0]],[[0, 0, 0, 0],
                                                         [0, 1, 1, 0],
                                                         [0, 1, 1, 0],
                                                         [0, 0, 0, 0]]]
jpieces = [[[0, 1, 1, 0],
            [0, 0, 1, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 0]],[[0, 0, 0, 0],
                           [0, 1, 1, 1],
                           [0, 1, 0, 0],
                           [0, 0, 0, 0]],[[0, 0, 1, 0],
                                          [0, 0, 1, 0],
                                          [0, 0, 1, 1],
                                          [0, 0, 0, 0]],[[0, 0, 0, 1],
                                                         [0, 1, 1, 1],
                                                         [0, 0, 0, 0],
                                                         [0, 0, 0, 0]]]
lpieces = [[[0, 0, 1, 0],
            [0, 0, 1, 0],
            [0, 1, 1, 0],
            [0, 0, 0, 0]],[[0, 0, 0, 0],
                           [0, 1, 1, 1],
                           [0, 0, 0, 1],
                           [0, 0, 0, 0]],[[0, 0, 1, 1],
                                          [0, 0, 1, 0],
                                          [0, 0, 1, 0],
                                          [0, 0, 0, 0]],[[0, 1, 0, 0],
                                                         [0, 1, 1, 1],
                                                         [0, 0, 0, 0],
                                                         [0, 0, 0, 0]]]
zpieces = [[[0, 1, 0, 0],
            [0, 1, 1, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 0]],[[0, 0, 0, 0],
                           [0, 1, 1, 0],
                           [1, 1, 0, 0],
                           [0, 0, 0, 0]],[[0, 1, 0, 0],
                                          [0, 1, 1, 0],
                                          [0, 0, 1, 0],
                                          [0, 0, 0, 0]],[[0, 0, 1, 1],
                                                         [0, 1, 1, 0],
                                                         [0, 0, 0, 0],
                                                         [0, 0, 0, 0]]]
spieces = [[[0, 0, 1, 0],
            [0, 1, 1, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 0]],[[0, 0, 0, 0],
                           [0, 1, 1, 0],
                           [0, 0, 1, 1],
                           [0, 0, 0, 0]],[[0, 0, 1, 0],
                                          [0, 1, 1, 0],
                                          [0, 1, 0, 0],
                                          [0, 0, 0, 0]],[[1, 1, 0, 0],
                                                         [0, 1, 1, 0],
                                                         [0, 0, 0, 0],
                                                         [0, 0, 0, 0]]]
tpieces = [[[0, 0, 1, 0],
            [0, 1, 1, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 0]],[[0, 0, 0, 0],
                           [0, 1, 1, 1],
                           [0, 0, 1, 0],
                           [0, 0, 0, 0]],[[0, 1, 0, 0],
                                          [0, 1, 1, 0],
                                          [0, 1, 0, 0],
                                          [0, 0, 0, 0]],[[0, 1, 0, 0],
                                                         [1, 1, 1, 0],
                                                         [0, 0, 0, 0],
                                                         [0, 0, 0, 0]]]

DEPTH_BOARD = 20
NUM_PIECES = [1, 2, 3, 4, 5, 6, 7]
MAP_NUM_PIECE = {1: ipieces, 2: opieces, 3: jpieces, 4: lpieces, 5: zpieces, 6: spieces, 7: tpieces}

def get_full_pos(piece):
    full_pos = []
    for x, row in enumerate(piece):
        for y, cell in enumerate(row):
            if cell == 1:
                full_pos.append((x, y))
    return full_pos


def check_collision(board, piece, px, py, w_b):
    # the top left of piece:
    # px is num of col in board
    # py is num of row in board
    full_pos = get_full_pos(piece)
    if len(full_pos) == 0:
        return True
    for pos in full_pos:
        x = pos[0]
        y = pos[1]
        if x + px > w_b - 1:  # bound right
            return True

        if x + px < 0:  # bound left
            return True

        if y + py > DEPTH_BOARD - 1:  # bound bottom
            return True

        if y + py < 0:
            continue

        if board[x + px][y + py] > 0:
            return True
    return False


def depth_drop(board, piece, px, py, w_b):
    depth = 0
    while True:
        if check_collision(board, piece, px, py + depth, w_b) is True:
            break
        depth += 1
    depth -= 1
    return depth



class Tetris:
    def __init__(self,w_b):
        self.board = np.zeros((DEPTH_BOARD, w_b), dtype=np.float32)
        self.index_block = random.randint(1, 7)
        self.current_block = MAP_NUM_PIECE[self.index_block][0]
        self.sub_index_block = 0
        self.next_blocks = NUM_PIECES
        # Position default
        self.px = 4
        self.py = 0
        self.width_board = w_b

        # define action
        self.action_meaning = {
            2: "drop",
            5: "right",
            6: "left"
        }

        # cleared
        self.cleared = 0
        # end game
        self.done = False

    def new_block(self):
        if len(self.next_blocks) == 0:
            blocks = deepcopy(NUM_PIECES)
            random.shuffle(blocks)
            self.next_blocks = deepcopy(blocks)
        self.index_block = self.next_blocks.pop(0)
        self.sub_index_block = 0
        self.current_block = MAP_NUM_PIECE[self.index_block][self.sub_index_block]
        self.px = 4
        self.py = 0

    def drop(self):
        depth_falling = depth_drop(board=self.board, piece=self.current_block, px=self.px, py=self.py, w_b = self.width_board)
        if depth_falling == -1:
            self.done = True
            return self.board, self.done
        self.py += depth_falling
        new_board = deepcopy(self.board)
        full_pos_block = get_full_pos(self.current_block)
        for pos in full_pos_block:
            x = pos[0]
            y = pos[1]
            new_board[self.px + x][self.py + y] = 1
        self.board = new_board
        self.clear()
        self.new_block()
        return new_board, self.done

    def rotate_right(self):
        self.sub_index_block += 1
        self.sub_index_block %= 4
        self.current_block = MAP_NUM_PIECE[self.index_block][self.sub_index_block]

    def rotate_left(self):
        self.sub_index_block += 3
        self.sub_index_block %= 4
        self.current_block = MAP_NUM_PIECE[self.index_block][self.sub_index_block]

    def move(self, action):
        # 5: right  ~ +1
        # 6: left   ~ -1
        # 3: rotate right
        # 4: rotate left
        # 2: drop
        # print(np.transpose(np.array(self.current_block)))
        if action == 2:
            return self.drop()
        if action == 5:
            if not check_collision(self.board, self.current_block, px=(self.px + 1), py=self.py, w_b = self.width_board):
                self.px += 1
        if action == 6:
            if not check_collision(self.board, self.current_block, px=(self.px - 1), py=self.py, w_b = self.width_board):
                self.px -= 1
        if action == 3:
            self.rotate_right()
        if action == 4:
            self.rotate_left()
        return self.board, self.done

    def clear(self):
        clear = 0
        for col in range(DEPTH_BOARD):
            cnt = 0
            for row in range(self.width_board):
                if self.board[row][col] == 1:
                    cnt += 1
            if cnt == self.width_board:
                clear += 1
                for i in range(self.width_board):
                    del self.board[i][col]
                    self.board[i] = [0] + self.board[i]
        self.cleared = clear

    def get_info_from_state(self):
        heights = []
        holes = []
        for row in range(self.width_board):
            height_row = 0
            for col in range(DEPTH_BOARD):
                if self.board[row][col] == 1:
                    height_row = DEPTH_BOARD - col
                    n_hol_in_col = 0
                    for col_hole in range(col + 1, DEPTH_BOARD):
                        if self.board[row][col_hole] == 0:
                            n_hol_in_col += 1
                    holes.append(n_hol_in_col)
                    break
            heights.append(height_row)

        # height sum
        height_sum = sum(heights)
        # diff sum
        diff_sum = 0
        for i in range(1, len(heights)):
            diff_sum += abs(heights[i] - heights[i - 1])

        # height max
        max_height = max(heights)

        # holes sum
        hole_sum = sum(holes)

        # deepest unfilled
        deepest_unfilled = min(heights)

        # blocks count
        blocks = 0
        for row in self.board:
            blocks += np.count_nonzero(np.array(row))
        blocks /= 4

        # col holes
        col_holes = np.count_nonzero(np.array(holes))

        # cleared
        cleared_num = self.cleared

        # pit hole percent
        pit = (self.width_board * DEPTH_BOARD - height_sum)
        pit_hole_percent = pit / (pit + hole_sum)

        return [height_sum, diff_sum, max_height, hole_sum, deepest_unfilled,
                blocks, col_holes, max(cleared_num + 9 - self.width_board,0), pit_hole_percent]

def initialize(obss):
    # initialize
    board = np.array(obss[:,:10,0],dtype=np.int32)
    holding = 0
    pieces = []

    new_board = (np.transpose(board)).tolist()

    # get the holding piece
    for i in range(10, 17):
        if obss[0][i][0] == 1:
            holding = i - 9

    # get next 5 pieces
    for j in range(1, 6):
        for i in range(10, 17):
            if obss[j][i][0] == 1:
                pieces.append(i - 9)
                break
    return new_board, holding, pieces

def get_a_possible_move_list(right=0, left=0, rot_right=0, rot_left=0):
    a_possible_move_list = rot_left *[4] + rot_right * [3] + right * [5] + left * [6] + [2]
    return a_possible_move_list

def get_possible_move_lists(possible_move_lists, nowblock):
    max_left = 4
    max_right = 3
    """extra"""
    newpossible_movelists = []
    for item in possible_move_lists:
        new_item = deepcopy(item)
        #1: ipieces, 2: opieces, 3: jpieces, 4: lpieces, 5: zpieces, 6: spieces, 7: tpieces
        if nowblock == 1:
            """ no rotate"""
            max_left = 4
            max_right = 2
            for left in range(0, max_left + 1):
                newpossible_movelists.append(new_item + get_a_possible_move_list(left=max_left-left))
            for right in range(1, max_right + 1):
                newpossible_movelists.append(new_item + get_a_possible_move_list(right=right))
            """rotate right: 1"""
            max_left = 6
            max_right = 3
            for left in range(0, max_left + 1):
                newpossible_movelists.append(new_item + get_a_possible_move_list(left=max_left-left, rot_right=1))
            for right in range(1, max_right + 1):
                newpossible_movelists.append(new_item + get_a_possible_move_list(right=right, rot_right=1))
        elif nowblock == 2:
            max_left = 6
            max_right = 3
            for left in range(0, max_left + 1):
                newpossible_movelists.append(new_item + get_a_possible_move_list(left=max_left-left))
            for right in range(1, max_right + 1):
                newpossible_movelists.append(new_item + get_a_possible_move_list(right=right))
        elif nowblock == 3 or nowblock == 4 or nowblock == 7:
            """no rotate"""
            max_left = 4
            max_right = 3
            for left in range(0, max_left + 1):
                newpossible_movelists.append(new_item + get_a_possible_move_list(left=max_left-left))
            for right in range(1, max_right + 1):
                newpossible_movelists.append(new_item + get_a_possible_move_list(right=right))
            """rotate left = 2"""
            max_left = 4
            max_right = 3
            for left in range(0, max_left + 1):
                newpossible_movelists.append(new_item + get_a_possible_move_list(left=max_left-left, rot_left=2))
            for right in range(1, max_right + 1):
                newpossible_movelists.append(new_item + get_a_possible_move_list(right=right, rot_left=2))
            """ rotate left 1"""
            max_left = 4
            max_right = 4
            for left in range(0, max_left + 1):
                newpossible_movelists.append(new_item + get_a_possible_move_list(left=max_left-left, rot_left=1))
            for right in range(1, max_right + 1):
                newpossible_movelists.append(new_item + get_a_possible_move_list(right=right, rot_left=1))
            """rotate right"""
            max_left = 5
            max_right = 3
            for left in range(0, max_left + 1):
                newpossible_movelists.append(new_item + get_a_possible_move_list(left=max_left-left, rot_right=1))
            for right in range(1, max_right + 1):
                newpossible_movelists.append(new_item + get_a_possible_move_list(right=right, rot_right=1))
        elif nowblock == 5 or nowblock == 6:
            """no rotate"""
            max_left = 4
            max_right = 3
            for left in range(0, max_left + 1):
                newpossible_movelists.append(new_item + get_a_possible_move_list(left=max_left-left))
            for right in range(1, max_right + 1):
                newpossible_movelists.append(new_item + get_a_possible_move_list(right=right))
            """rotate_right"""
            max_left = 5
            max_right = 3
            for left in range(0, max_left + 1):
                newpossible_movelists.append(new_item + get_a_possible_move_list(left=max_left-left, rot_right=1))
            for right in range(1, max_right + 1):
                newpossible_movelists.append(new_item + get_a_possible_move_list(right=right, rot_right=1))
            """rotate left"""
            max_left = 4
            max_right = 4
            for left in range(0, max_left + 1):
                newpossible_movelists.append(new_item + get_a_possible_move_list(left=max_left-left, rot_left=1))
            for right in range(1, max_right + 1):
                newpossible_movelists.append(new_item + get_a_possible_move_list(right=right, rot_left=1))
    return newpossible_movelists

def get_rating_from_move(board, list_block, list_move, gen, width_board, mode):
    game_check = Tetris(width_board)
    game_check.board = board
    game_check.clear()
    extra_height = game_check.cleared
    game_check.cleared = 0
    game_check.index_block = list_block[0]
    game_check.next_blocks = list_block[1:]
    game_check.current_block = MAP_NUM_PIECE[game_check.index_block][0]
    done = False
    state_board = game_check.board
    for one_move in list_move:
        state_board, done = game_check.move(one_move)
        if done == True:
            break
    info = game_check.get_info_from_state()
    rating = -200000000 * info[3]
    if game_check.cleared == 1:
        rating -= 30
    for i in range(len(info)):
        rating += info[i]*gen[i]
    if info[2] + extra_height >= 16:
        rating -= 200
    if done:
        rating -= 200
    return rating

from itertools import chain
def top_move(board, list_block, firstmove, possible_move_lists , gen, width_board, mode, top=4):
    record = []
    for cur_list in possible_move_lists:
        move = deepcopy(firstmove)
        move.append(cur_list)
        cur_rating = get_rating_from_move(board, list_block, list(chain.from_iterable(move)), gen, width_board, mode)
        record.append([cur_rating, move])
    record.sort()
    record = record[-top:]
    toprecord = []
    for i in range(len(record)):
        toprecord.append(record[i][1])
    return [toprecord,record[0][0]]

def get_best_move(board, list_block, gen, width_board, mode):
    best_list = []
    best = -20000000000
    #-------------------------------------------------------------------------------------------------------------
    possible_move_lists_bl0 = get_possible_move_lists([[]], list_block[0])
    possible_move_lists_bl1 = get_possible_move_lists([[]], list_block[1])
    possible_move_lists_bl2 = get_possible_move_lists([[]], list_block[2])
    possible_move_lists_bl3 = get_possible_move_lists([[]], list_block[3])
    #-------------------------------------------------------------------------------------------------------------
    record1step = top_move(board, [list_block[0],7], [], possible_move_lists_bl0 , gen, width_board, mode,5)
    for step1 in record1step[0]:
        record2step = top_move(board, [list_block[0],list_block[1]], step1, possible_move_lists_bl1 , gen, width_board, mode,2)
        for step2 in record2step[0]:
            record3step = top_move(board, [list_block[0],list_block[1],list_block[2]], step2, possible_move_lists_bl2 , gen, width_board, mode)
            if(record3step[1]> best):
                best = record3step[1]
                best_list =[1] + record3step[0][0][0]
            record3step = top_move(board, [list_block[0],list_block[1],list_block[3]], step2, possible_move_lists_bl3 , gen, width_board, mode)
            if(record3step[1]> best):
                best = record3step[1]
                best_list =[1] + record3step[0][0][0]

        record2step = top_move(board, [list_block[0],list_block[2]], step1, possible_move_lists_bl2 , gen, width_board, mode,2)
        for step2 in record2step[0]:
            record3step = top_move(board, [list_block[0],list_block[2],list_block[1]], step2, possible_move_lists_bl1 , gen, width_board, mode)
            if(record3step[1]> best):
                best = record3step[1]
                best_list =[1] + record3step[0][0][0]
            record3step = top_move(board, [list_block[0],list_block[2],list_block[3]], step2, possible_move_lists_bl3 , gen, width_board, mode)
            if(record3step[1]> best):
                best = record3step[1]
                best_list =[1] + record3step[0][0][0]
    #-------------------------------------------------------------------------------------------------------------
    record1step = top_move(board, [list_block[1],7], [], possible_move_lists_bl1 , gen, width_board, mode,5)
    for step1 in record1step[0]:
        record2step = top_move(board, [list_block[1],list_block[0]], step1, possible_move_lists_bl0 , gen, width_board, mode,2)
        for step2 in record2step[0]:
            record3step = top_move(board, [list_block[1],list_block[0],list_block[2]], step2, possible_move_lists_bl2 , gen, width_board, mode)
            if(record3step[1]> best):
                best = record3step[1]
                best_list = record3step[0][0][0]
            record3step = top_move(board, [list_block[1],list_block[0],list_block[3]], step2, possible_move_lists_bl3 , gen, width_board, mode)
            if(record3step[1]> best):
                best = record3step[1]
                best_list = record3step[0][0][0]

        record2step = top_move(board, [list_block[1],list_block[2]], step1, possible_move_lists_bl2 , gen, width_board, mode,2)
        for step2 in record2step[0]:
            record3step = top_move(board, [list_block[1],list_block[2],list_block[0]], step2, possible_move_lists_bl0 , gen, width_board, mode)
            if(record3step[1]> best):
                best = record3step[1]
                best_list = record3step[0][0][0]
            record3step = top_move(board, [list_block[1],list_block[2],list_block[3]], step2, possible_move_lists_bl3 , gen, width_board, mode)
            if(record3step[1]> best):
                best = record3step[1]
                best_list = record3step[0][0][0]
    return best_list

class Agent:
    def __init__(self, turn):
        self.list_move = []
        self.gen = [-0.45871856486636053, -0.3211088438566083, -0.5221084651717414, -1.4317746855089484, -0.8248875964891864, 1.856227466507848, -1.59595104909416, 0.7765780163107312, 1.8598908998668202, 2001, 500, 500]
        self.list_block = [1]
        self.best_score = -500000
        self.first = 1
        self.width_board = 9

    def choose_action(self, obs):
        if np.sum(np.array(obs[10,:10,0])) > 0:
            self.width_board = 10
        else:
            self.width_board = 9
        if self.first == 1:
            board, holding, pieces = initialize(obs)
            self.list_block = pieces[:3]
            self.first = 0
            return 1
        if len(self.list_move) == 1:
            board, holding, pieces = initialize(obs)
            self.list_block = pieces[:3]
        if len(self.list_move) == 0:
            board, holding, pieces = initialize(obs)
            self.list_move = get_best_move(board, [holding, self.list_block[0], self.list_block[1],self.list_block[2]], self.gen, self.width_board, 10 - self.width_board)
        action = self.list_move.pop(0)
        return action
