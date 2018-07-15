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

# At a push (8)
shelf1928_level11 = u"""
    xxxxv
 xxxp    x
x   xxx  x
x   ♀ p  x
x    xx  x
xd  ♂xxxx
x    x
 xxxx
"""

# Down to Earth
shelf1937_level1 = u"""
  x  xp   x
  x  xx   x
 xx  g    xx
xxxxxxxxpxxxx
xxxxxx    xxx
 xxpg d xxxx
  x x  x  x
  x  x    x
"""

# Illusion of Choice
shelf1937_level2 = u"""
xxxxxxx
  xp
x xgx x
xpgdgpx
x xgx x
xx p xx
xxxxxxx
"""

# More Haste
shelf1937_level3 = u"""
  p      p
 x        x

 x p gg pdx
x x      x x
x        x
 x        x
"""

# Worth its Weight
shelf1937_level4 = """
xxxxxxxxxxxxxxx
xx p    x   xxx
x    px   xp xx
x   p  xp     x
xxd  x     x xx
xxx  px  x pxxx
xxxxxxxxxxxxxxx
"""

# Tunnel Vision
shelf1937_level5 = """
xxxxxxxxxxxxxxx
x g g g g   p x
xgxxxxxxx xxxxx
x   g   x  pg x
x xxx x xdxxx x
x xxx xgxxx g x
xpxp  x  gp xxx
xxxxxxxxxxxxxxx
"""

# The Trap
shelf1937_level6 = """
  xxxxxxxxxxx
  >    p    <
         xx
       d  xp  p
   +     xx
      xxxp  x
         x xx
"""

# Open and Shut Case
shelf1937_level7 = """
   g
dgp
  g
g  p
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

    def test_shelf1928_level11(self):
        self.solution_should_be(
            shelf1928_level11,
            [],
        )
    del test_shelf1928_level11

    def test_shelf1937_level1(self):
        self.solution_should_be(
            shelf1937_level1,
            ['left', 'down', 'right', 'up', 'left', 'down', 'left', 'down'],
        )

    def test_shelf1937_level2(self):
        self.solution_should_be(
            shelf1937_level2,
            ['right', 'up', 'right', 'down', 'up', 'left', 'down'],
        )

    def test_shelf1937_level3(self):
        self.solution_should_be(
            shelf1937_level3,
            ['up', 'down', 'left', 'up'],
        )

    def test_shelf1937_level4(self):
        self.solution_should_be(
            shelf1937_level4,
            ['right', 'down', 'right', 'left', 'up', 'right', 'down', 'right',
             'up', 'right', 'down', 'left', 'up', 'right', 'down', 'left',
             'up', 'left', 'up', 'right', 'down', 'right', 'down', 'right',
             'down', 'right'],
        )

    def test_shelf1937_level5(self):
        self.solution_should_be(
            shelf1937_level5,
            ['up', 'right', 'left', 'down', 'up', 'right', 'left', 'down',
             'left', 'right', 'up', 'right', 'down', 'right', 'up', 'right',
             'up', 'left'],
        )

    def test_shelf1937_level6(self):
        self.solution_should_be(
            shelf1937_level6,
            ['left', 'down', 'left', 'right', 'up', 'left'],
        )

    def test_shelf1937_level7(self):
        self.solution_should_be(
            shelf1937_level7,
            [],
        )
    del test_shelf1937_level7

if __name__ == '__main__':
    unittest.main()
