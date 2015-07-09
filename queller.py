#!/usr/bin/env python

from collections import defaultdict

# Quell levels

# Introduction
shelf1928_level1 = """
  x xxxxx
 x    p  x
x p d   pxx
 x    px x
  x x x x
"""

# Easy going
shelf1928_level2 = """
 xxxxxxxx
xxp      x
xp        x
 x        x
  xxxxx   x
      x   x
      xpd x
       xxx
"""

# Side to side
shelf1928_level3 = """
xxxxxxxxxxx
  p xxxp
     x
  d  xp
  x  x   x
    pxx
    xxxx
xxxxxxxxxxx
"""

# No way back
shelf1928_level4 = """
 xxxxxxxxx
xxp  x   xx
x x  x x  x
x  p g    x
x    x    x
xxd  x  pxx
 xxxxxxxxx
"""

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


class Drop(object):
    def __init__(self, board):
        self.board = board
        self.position = (None, None)


class Board(object):
    def __init__(self, level, drops_positions, remaining_pearls, width=None, height=None):
        # Note, no copy; client is supposed to provide one
        self.level = level

        if width is None:
            self.width = max(len(line) for line in level)
        else:
            self.width = width

        if height is None:
            self.height = len(level)
        else:
            self.height = height

        # {which -> (x, y)}
        # Note, see above
        self.drops_positions = drops_positions

        self.remaining_pearls = remaining_pearls

    @staticmethod
    def fromString(level_str):
        level = []
        width = 0
        for line in level_str.split('\n')[1:-1]:
            level.append(list(line))
            width = max(width, len(line))

        # Pad until all rows are max width long.
        for line in level:
            while len(line) < width:
                line.append(' ')

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

    def nextDropPos(self, pos, dx, dy):
        # Apply direction and update drop position, keeping wraps into
        # account
        if pos[0] == 0 and dx == -1:
            next_pos_x = self.width - 1
            next_pos_y = pos[1] + dy

        elif pos[0] == self.width - 1 and dx == 1:
            next_pos_x = 0
            next_pos_y = pos[1] + dy

        elif pos[1] == 0 and dy == -1:
            next_pos_x = pos[0] + dx
            next_pos_y = self.height - 1

        elif pos[1] == self.height - 1 and dy == 1:
            next_pos_x = pos[0] + dx
            next_pos_y = 0

        else:
            next_pos_x = pos[0] + dx
            next_pos_y = pos[1] + dy

        assert 0 <= next_pos_x <= self.width - 1
        assert 0 <= next_pos_y <= self.height - 1

        next_pos = next_pos_x, next_pos_y

        return next_pos

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

            next_pos = self.nextDropPos(pos, dx, dy)

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
            elif next_block == "g":
                # A gate. Change this into a block and assume it's fine to
                # forcefully move the drop ahead.
                new_level[pos[1]][pos[0]] = " "
                new_level[next_pos[1]][next_pos[0]] = "x"

                next_pos = self.nextDropPos(next_pos, dx, dy)
                new_level[next_pos[1]][next_pos[0]] = "d"

                new_drops_positions["d"] = next_pos
                moved = True
                continue
            else:
                assert False, next_block

        if moved:
            return Board(new_level, new_drops_positions, new_remaining_pearls, self.width, self.height)

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
            # No copy!
            self.moves = moves
        self.n_moves = len(self.moves)

    def __repr__(self):
        g = self.n_moves
        h = self.board.remaining_pearls
        return "Solution(f=%s, g=%s, h=%s)" % (g + h, g, h)


class SolutionDict(object):

    def __init__(self):
        self._dict = defaultdict(list)
        self._indices = defaultdict(int)

    def append(self, solution):
        self.ordered_insert(solution)

    def popleft(self):
        # doesn't actually delete the popped item - we still need that
        # for duplicate check in ordered_insert
        for m in sorted(self._dict):
            idx = self._indices[m]
            l = self._dict[m]
            if idx < len(l):
                rv = l[idx]
                self._indices[m] += 1
                break

        return rv

    def ordered_insert(self, solution):
        # f = g + h
        f = solution.n_moves + solution.board.remaining_pearls

        # Check for equal board states but with less moves: don't add this
        # if we find one - note: this is crucial to get decent computing times

        for m in sorted(self._dict):
            if m < f:
                for ss in self._dict[m]:
                    if ss.board.level == solution.board.level:
                        return
            else:
                break

        self._dict[f].append(solution)


class Searcher(object):
    def __init__(self, board):
        self.board = board

    def search(self):
        self.solutions = SolutionDict()
        self.solutions.append(Solution(self.board))

        depth = 0

        while self.solutions:
            s = self.solutions.popleft()

            board = s.board
            moves = s.moves

            if s.n_moves > depth:
                depth = s.n_moves
                print depth

            if board.remaining_pearls == 0:
                print moves
                return

            for direction in ("up", "down", "left", "right"):
                next_board = board.move("d", direction)
                if next_board is None:
                    continue

                new_solution = Solution(next_board, moves + [direction])

                # Ordered insert
                self.solutions.ordered_insert(new_solution)

if __name__ == "__main__":
    board = Board.fromString(levelx)
    searcher = Searcher(board)
    searcher.search()
