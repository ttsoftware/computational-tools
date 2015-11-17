import argparse
import unittest

import sys

from src.exercise_1 import exercise_1
from src.exercise_2 import exercise_2
from src.exercise_3 import exercise_3


class WordCountTest(unittest.TestCase):

    def test_exercise_1(self):

        sys.argv[1] = "../data/words.txt"
        sys.argv[2] = "-q"

        exercise_1().run()

    def test_exercise_2(self):

        sys.argv[1] = "../data/euler_graph_1.txt"
        sys.argv[2] = "-q"
        exercise_2().run()

        sys.argv[1] = "../data/euler_graph_2.txt"
        exercise_2().run()

        sys.argv[1] = "../data/euler_graph_3.txt"
        exercise_2().run()

        sys.argv[1] = "../data/euler_graph_4.txt"
        exercise_2().run()

        sys.argv[1] = "../data/euler_graph_5.txt"
        exercise_2().run()

    def test_exercise_3(self):

        sys.argv.append("../data/facebook_combined.txt")
        #sys.argv.append("--base-tmp-dir=../data/output")
        #sys.argv.append("--cleanup=NONE")
        sys.argv.append("--output-dir=../data/output")

        exercise_3().run()