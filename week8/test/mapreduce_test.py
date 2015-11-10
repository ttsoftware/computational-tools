import argparse
import unittest

import sys

from src.exercise_1 import exercise_1
from src.exercise_2 import exercise_2


class WordCountTest(unittest.TestCase):

    def test_exercise_1(self):

        sys.argv[1] = "../data/words.txt"
        sys.argv[2] = "-q"

        exercise_1().run()

    def test_exercise_2(self):

        sys.argv[1] = "../data/euler_graph_1.txt"
        sys.argv[2] = "-q"

        exercise_2().run()