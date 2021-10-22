import unittest
import main

class TestMain(unittest.TestCase):

    def test_hello_world(self):
        
        self.assertEqual(main.the_string, ("hello world"))

    def test_starting_up(self):
        self.assertEqual(main.starting_up(), "hello world")


if __name__ == '__main__':
    unittest.main()