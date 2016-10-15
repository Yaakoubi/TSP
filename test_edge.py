from edge import Edge
import unittest
from node import Node


class TestEdgeMethods(unittest.TestCase):
    """ Teste les differentes fonctions de la classe Edge."""

    n1 = Node(name="test1")
    n2 = Node(name="test2")
    n3 = Node(name="test3")

    def setUp(self):
        """ Liste de commandes qui sera lancee a chaque test """
        self.edg_test1 = Edge("edge_test1", [self.n1, self.n2, 79])
        self.edg_test2 = Edge(data=[self.n2, self.n3], name="edge_test2")
        self.edg_test3 = Edge("edge_test2")
        self.edg_test4 = Edge("edge_test4", [])
        self.edg_def = Edge()

    def test_get_name(self):
        """ Verification du nom renvoye par la fonction get_name. """
        self.assertEqual('Sans nom', self.edg_def.get_name())
        self.assertEqual('edge_test1', self.edg_test1.get_name())
        self.assertEqual('edge_test2', self.edg_test2.get_name())

    def test_get_data(self):
        """ Verification que le pointeur de donnees renvoie vers quelque chose. """
        self.failUnless(self.edg_def.get_data() is not None)
        self.failUnless(self.edg_test2.get_data() is not None)

    def test_get_start(self):
        """ Verification que le pointeur de donnees renvoie vers quelque chose. """
        self.failUnless(self.edg_def.start is None)
        self.failUnless(self.edg_test3.start is None)
        self.failUnless(self.edg_test4.start is None)
        self.failUnless(self.edg_test2.start is not None)

    def test_get_end(self):
        """ Verification que le pointeur de donnees renvoie vers quelque chose. """
        self.failUnless(self.edg_def.end is None)
        self.failUnless(self.edg_test2.end is not None)
        self.failUnless(self.edg_test4.end is None)

    def test_get_weight(self):
        """ Verification que le pointeur de donnees renvoie vers quelque chose. """
        self.failUnless(self.edg_def.weight is None)
        self.failUnless(self.edg_test2.weight is None)

    def test_set_start(self):
        """ Verification que le pointeur de donnees renvoie vers quelque chose. """
        self.edg_def.start = Node()
        self.edg_test2.start = Node()
        self.failUnless(self.edg_def.start is not None)
        self.failUnless(self.edg_test2.start is not None)

    def test_set_end(self):
        """ Verification que le noeud d'arrivee est bien affecte"""
        self.edg_def.end = self.n1
        self.edg_test2.end = self.n2
        self.edg_test4.end = []
        self.failUnless( self.edg_def.end == self.n1 )
        self.failUnless( self.edg_test2.end == self.n2 )
        self.failUnless( self.edg_test3.end is None )
        self.failUnless( self.edg_test4.end is None )


    def test_set_weight(self):
        """ Verification que le poids est bien affecte"""
        self.edg_def.weight = 5
        self.edg_test2.weight = 7
        self.failUnless(self.edg_def.weight == 5)
        self.failUnless(self.edg_test2.weight == 7)

if __name__ == '__main__':
    unittest.main()
