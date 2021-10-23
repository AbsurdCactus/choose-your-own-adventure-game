import unittest
import main

class TestMain(unittest.TestCase):

    def test_hello_world(self):
        
        self.assertEqual(main.the_string, ("hello world"))

    def test_starting_up(self):
        self.assertEqual(main.starting_up(), "hello world")

    def test_first_choice(self):
        self.assertEqual(main.first_choice("L"), "left")


if __name__ == '__main__':
    unittest.main()