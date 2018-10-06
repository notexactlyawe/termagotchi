from termagotchi.screen import Screen
from test.test_helper import captured_output
import unittest
import pdb

class TestScreenMethods(unittest.TestCase):
    def setUp(self):
        self.screen = Screen()

    def test_place_and_clear_gives_empty_screen(self):
        with captured_output() as (out, _):
            self.screen.draw()
        # strip - because we draw a line of hyphens at the bottom of the screen
        output = out.getvalue().strip().strip('-')
        self.assertEqual(output, "")

        self.screen.place("hello", 0, 0)
        self.screen.clear()
        with captured_output() as (out, _):
            self.screen.draw()
        output = out.getvalue().strip().strip('-')
        self.assertEqual(output, "")

if __name__ == "__main__":
    unittest.main()
