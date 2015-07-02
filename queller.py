#!/usr/bin/env python

from collections import deque

level1 = """
  xxxxx
  xxpxx
  x   x
  x d x
xx     xx
x  p xp x
x       x
xxxxxxxxx
"""

levelx = """
xxxxxxxxxxxxxxx
xx p    x   xxx
x    px   xp xx
x   p  xp     x
xxd  x     x xx
xxx  px  x pxxx
xxxxxxxxxxxxxxx
"""

DROPS = ["d"]

class InsDeque(deque):

    def insert(self, index, value):
        self.rotate(-index)
        self.appendleft(value)
        self.rotate(index)

class Type(object):
    BLOCK = 0
    PEARL = 1
    TOPAZ = 2
    GOLD = 3
    RING = 4

class DropState(object):
    NORMAL = 0
    GOLD = 1

class Drop(object):
    def __init__(self, board):
        self.board = board
        self.position = (None, None)
        self.state = DropState.NORMAL

    def move(self, direction):
        # If it's possible to move there, update position and drop state
        ok = self.board.move(self, direction)
        if not ok:
            return False

class Board(object):
    def __init__(self, level, drops_positions, remaining_pearls):
        # Note, no copy; client is supposed to provide one
        self.level = level

        # {which -> (x, y)}
        # Note, see above
        self.drops_positions = drops_positions

        self.remaining_pearls = remaining_pearls

    @staticmethod
    def fromString(level):
        level = [list(line) for line in level.split('\n')][1:-1]
        drops_positions = {}
        for dd in DROPS:
            pos = Board.getDropPosition(dd, level)
            drops_positions[dd] = pos
        remaining_pearls = Board.remainingPearls(level)
        return Board(level, drops_positions, remaining_pearls)

    @staticmethod
    def remainingPearls(level):
        pearls = 0
        for line in level:    
            for c in line:
                if c == "p":
                    pearls += 1
        return pearls

    @staticmethod
    def getDropPosition(which, level):
        for y, line in enumerate(level):
            for x, c in enumerate(line):
                if c == which:
                    return (x, y)
        raise RuntimeError()

    def move(self, drop, step):
        assert step in ("up", "down", "left", "right")

        moved = False

        new_level = []
        for line in self.level:
            new_level.append(line[:])

        new_drops_positions = self.drops_positions.copy()
        new_remaining_pearls = self.remaining_pearls

        dx = {"left": -1, "right": 1}.get(step, 0)
        dy = {"up": -1, "down": 1}.get(step, 0)

        while True:

            pos = new_drops_positions[drop]

            next_pos = pos[0] + dx, pos[1] + dy
            next_block = new_level[next_pos[1]][next_pos[0]]

            # Check various kinds of blocks:

            if next_block == " ":
                # Next block is free, go on
                new_level[pos[1]][pos[0]] = " "
                new_level[next_pos[1]][next_pos[0]] = "d"
                new_drops_positions["d"] = next_pos
                moved = True
                continue
            elif next_block == "p":
                # We got a pearl
                new_level[pos[1]][pos[0]] = " "
                new_level[next_pos[1]][next_pos[0]] = "d"
                new_drops_positions["d"] = next_pos
                new_remaining_pearls -= 1
                moved = True
                continue
            elif next_block == "x":
                # We can't move there, stop
                break
            else:
                assert False, next_block

        if moved:
            return Board(new_level, new_drops_positions, new_remaining_pearls)

        return None

    def __str__(self):
        st = ""
        for l in self.level:
            for c in l:
                st += c
            st += '\n'
        return st

class Solution(object):
    def __init__(self, board, moves=None):
        self.board = board
        if moves is None:
            self.moves = []
        else:
            self.moves = moves[:]
        self.n_moves = len(self.moves)

class Searcher(object):
    def __init__(self, board):
        self.board = board

    def heur(self, solution):
        return solution.board.remaining_pearls

    def steps(self, solution):
        return solution.n_moves + self.heur(solution)

    def search(self):
        self.solutions = InsDeque()
        self.solutions.append(Solution(self.board))

        depth = 0

        while self.solutions:
            s = self.solutions.pop()

            board = s.board
            moves = s.moves

            if s.n_moves > depth:
                depth = s.n_moves
                print depth

            if board.remaining_pearls == 0:
                print moves
                print "done!"
                return

            for direction in ("up", "down", "left", "right"):
                next_board = board.move("d", direction)
                if next_board is None:
                    continue

                new_solution = Solution(next_board, moves + [direction])
                cur_f = self.steps(new_solution)

                # Ordered insert
                ii = 0
                for ii, ss in enumerate(self.solutions):
                    target_f = self.steps(ss)
                    if cur_f > target_f:
                        break
                self.solutions.insert(ii, new_solution)

if __name__ == "__main__":
    board = Board.fromString(levelx)
    searcher = Searcher(board)
    searcher.search()
