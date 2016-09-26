""" Fichier de tests unitaires. """

# from edge import Edge
# from node import Node
# from graph import Graph
import unittest
import random

class TestEdgeMethods(unittest.TestCase):


    def test_get_name(self):
        default = Edge()
        # self.assertIn(elt,liste)
        self.assertEqual('no_name', default.get_name)

    # def test_isupper(self):
    #     self.assertTrue('FOO'.isupper())
    #     self.assertFalse('Foo'.isupper())
    #
    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)

if __name__ == '__main__':
    unittest.main()
