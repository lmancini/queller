#!/usr/bin/env python
# coding: utf-8

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

# Look sharp
shelf1928_level5 = """
xxxxxxxxx
xxxxxx     <
 > p     xx
 x   d  p x
 xx       x
xxx   p p x
xxxxxxxxx
"""

# The blunt truth
shelf1928_level6 = """
   xx   xx
  xxxxxxxxx
 xxvp    vxx
xx         xx
xx d       xx
 xx p ^  p x
  xxxxxxxxx
   xx   xx
"""

# One way
shelf1928_level7 = """
        pxxxx
  xxx    v xx
    xx>    xx
   pxx>  d p
    xx>    xx
   p
        xxxxx
"""

# Frozen
shelf1928_level8 = """
xxxxxxxxxxxx
xv      xpxx
x  g d     x
x          x
xp         x
xx   +    xx
xxxxxxxxxxxx
"""

# A certain ring
shelf1928_level9 = """
 xxxxx
x    ox
x  pxxx
xx xxpx
x dxo x
 xxxxx
"""

# Step in the right direction
shelf1928_level10 = """
  xxx   xx
 xv  xxx  x
xx  xxxx  xx
xxop xp  oxx
xx   xxx  xx
 x  pxxxd x
  xxx   xx
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

    def test_shelf1928_level5(self):
        self.solution_should_be(
            shelf1928_level5,
            ['up', 'right', 'down', 'left', 'up'],
        )

    def test_shelf1928_level6(self):
        self.solution_should_be(
            shelf1928_level6,
            ['right', 'down', 'left', 'up', 'left', 'down'],
        )

    def test_shelf1928_level7(self):
        self.solution_should_be(
            shelf1928_level7,
            ['right', 'down', 'right'],
        )

    def test_shelf1928_level8(self):
        self.solution_should_be(
            shelf1928_level8,
            ['left', 'down', 'right', 'up', 'left', 'up', 'right', 'down', 'right', 'up'],
        )

    def test_shelf1928_level9(self):
        self.solution_should_be(
            shelf1928_level9,
            ['up', 'right', 'up', 'down', 'left', 'down', 'right'],
        )

    def test_shelf1928_level10(self):
        self.solution_should_be(
            shelf1928_level10,
            ['up', 'right', 'down', 'right', 'up', 'left'],
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
