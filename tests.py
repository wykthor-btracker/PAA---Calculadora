# -*- encoding: utf-8 -*-

# # imports
import big
import unittest
from random import randint
# # imports

# # variables

# # variables

# # classes


class TestBigNumber(unittest.TestCase):
    def test_sum(self):
        x, y = randint(0, 2**64), randint(0, 2**64)
        a, b = big.BigNumber(str(x)), big.BigNumber(str(y))
        self.assertEqual(int(a+b), x+y)


# # classes

# # functions

# # functions

# # main
def main(*args, **kwargs):
    return


# # main 

if __name__ == "__main__":
    main()