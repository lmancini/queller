#!/usr/bin/env python

from queller import Board
from queller import Searcher
import unittest

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

# Worth its weight
shelf1937_level4 = """
xxxxxxxxxxxxxxx
xx p    x   xxx
x    px   xp xx
x   p  xp     x
xxd  x     x xx
xxx  px  x pxxx
xxxxxxxxxxxxxxx
"""


class TestQueller(unittest.TestCase):

    def solution_should_be(self, level, solution):
        board = Board.fromString(level)
        searcher = Searcher(board)
        moves = searcher.search()

        self.assertEqual(moves, solution)

    def test_shelf1928_level1(self):
        self.solution_should_be(
            shelf1928_level1,
            ['right', 'up', 'left', 'down', 'right'],
        )

    def test_shelf1928_level2(self):
        self.solution_should_be(
            shelf1928_level2,
            ['left', 'up', 'left', 'down', 'right', 'up', 'left'],
        )

    def test_shelf1928_level3(self):
        self.solution_should_be(
            shelf1928_level3,
            ['left', 'right', 'down', 'left', 'up', 'right'],
        )

    def test_shelf1928_level4(self):
        self.solution_should_be(
            shelf1928_level4,
            ['right', 'up', 'left', 'right', 'down', 'left', 'up', 'right',
             'up', 'left', 'down'],
        )

    def test_shelf1937_level4(self):
        self.solution_should_be(
            shelf1937_level4,
            ['right', 'down', 'right', 'left', 'up', 'right', 'down', 'right',
             'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left',
             'up', 'left', 'up', 'right', 'down', 'right', 'down', 'right',
             'down', 'right'],
        )

if __name__ == '__main__':
    unittest.main()
