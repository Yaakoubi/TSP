from edge import Edge
import unittest
# import random


class TestEdgeMethods(unittest.TestCase):
    """ Teste les differentes fonctions de la classe Edge."""

    def setUp(self):
        """ Liste de commandes qui sera lancee a chaque test """
        self.edg_test1 = Edge("edge_test1", [34, 45, 79])
        self.edg_test2 = Edge(data = (1,2), name="edge_test2")
        self.edg_def = Edge()

    def test_get_name(self):
        """ Verification du nom renvoye par la fonction get_name. """
        self.assertEqual('Sans nom', self.edg_def.get_name())
        self.assertEqual('edge_test1', self.edg_test1.get_name())
        self.assertEqual('edge_test2', self.edg_test2.get_name())

    def test_get_id(self):
        """ Verification que l'indice d'une arete est un nombre entier. """
        self.assertTrue(type(self.edg_test1.get_id()) is int)
        self.assertEqual(self.edg_test2.get_id(), 4)

    def test_get_data(self):
        """ Verification que le pointeur de donnees renvoie vers quelquechose. """
        self.failUnless(self.edg_def.get_data() is None)
        self.failUnless(self.edg_test2.get_data() is not None)

    def test_repr(self):
        """ Verification qu'une chaine de caracteres est bien renvoyee a l'affichage par le module print. """
        self.assertTrue(type(self.edg_def.__repr__()) is str)

if __name__ == '__main__':
    unittest.main()

