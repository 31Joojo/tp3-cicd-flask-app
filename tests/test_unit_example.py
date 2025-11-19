import unittest

from src.app import items


class FirstUnitTest(unittest.TestCase):
    def test_adding_item(self):
        items.clear()

        # Adding some items in the list of items
        items.append('test_item1')
        items.append('test_item2')
        items.append('test_item3')

        self.assertEqual(len(items), 3)


if __name__ == '__main__':
    unittest.main()
