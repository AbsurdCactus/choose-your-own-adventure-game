import unittest
import main
from unittest.mock import patch
from io import StringIO


class TestMain(unittest.TestCase):

    # incomplete
    # this proves I can use a mock input
    def test_first_step(self):

        string_of_input = "L"

        with patch('sys.stdout', new=StringIO()) as fake_out:
            main.first_step()
            self.assertEqual(fake_out.getvalue(
            ), "Type \"left\" to go left, \"right\" to go right: \nYou fall into a hole. Game over\n")

    def test_gooby(self):

        # complete
        # this proves I can test printed values
        with patch('sys.stdout', new=StringIO()) as fake_out:
            main.gooby()
            self.assertEqual(fake_out.getvalue(), "hello world\n")


if __name__ == '__main__':
    unittest.main()
