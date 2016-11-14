from node import Node
import unittest
# import random


class TestNodeMethods(unittest.TestCase):
    """ Teste les differentes fonctions de la classe Node"""

    def setUp(self):
        """ Liste de commandes qui sera lancee a chaque test """
        self.nod_test1 = Node("node_test1", [34, 45, 79])
        self.nod_test2 = Node(data=(1, 2), name="node_test2")
        self.nod_test2.father = self.nod_test1
        self.nod_def = Node()

    def test_get_name(self):
        """ Verification du nom renvoye par la fonction get_name """
        self.assertEqual('Sans nom', self.nod_def.get_name())
        self.assertEqual('node_test1', self.nod_test1.get_name())
        self.assertEqual('node_test2', self.nod_test2.get_name())

    def test_get_id(self):
        """ Verification que l'indice d'une arete est un nombre entier """
        self.assertTrue(isinstance(self.nod_test1.get_id(), int))
        # self.assertEqual(self.nod_test2.get_id(), 7)

    def test_get_data(self):
        """ Verification que le pointeur de donnees renvoie vers quelque chose """
        self.failUnless(self.nod_def.get_data() is None)
        self.failUnless(self.nod_test2.get_data() is not None)

    def test_get_father(self):
        """ Verification de ce qu'il y a dans l'attribut father"""
        self.failUnless(self.nod_def.father == self.nod_def)
        self.failUnless(self.nod_test2.father == self.nod_test1)

    def test_get_prim_father(self):
        """ Verification de ce qu'il y a dans l'attribut prim_father"""
        self.nod_test2.prim_father = self.nod_test1
        self.failUnless(self.nod_def.prim_father is None)
        self.failUnless(self.nod_test2.prim_father == self.nod_test1)

    def test_get_ancestor(self):
        """ Verification de ce qu'il y a dans l'attribut father"""
        self.failUnless(self.nod_def.ancestor == self.nod_def)
        self.failUnless(self.nod_test2.ancestor == self.nod_test1)

    def test_repr(self):
        """ Verification qu'une chaine de caracteres est bien renvoyee a l'affichage par le module print """
        self.assertTrue(isinstance(self.nod_def.__repr__(), str))

    def test_rank(self):
        """ Verification du rang d'un noeud"""
        self.nod_test1.rank = 2
        self.failUnless(self.nod_def.rank == 0)
        self.failUnless(self.nod_test1.rank == 2)

    def test_min_weight(self):
        """Verification du poids minimum d'un noeud (pour l'algorithme de Prim)"""
        self.nod_test1.min_weight = 0
        self.failUnless(self.nod_def.min_weight == float('infinity'))
        self.failUnless(self.nod_test1.min_weight == 0)

    def test_comparison(self):
        """Verification de des comparaisons entre les noeuds"""
        self.nod_test1.min_weight = 0
        self.failUnless(self.nod_def >= self.nod_test1)
        self.failIf(self.nod_test1 >= self.nod_def)
        self.failUnless(self.nod_def > self.nod_test1)
        self.failIf(self.nod_test1 > self.nod_def)
        self.failUnless(self.nod_test1 <= self.nod_def)
        self.failIf(self.nod_def <= self.nod_test1)
        self.failUnless(self.nod_test1 < self.nod_def)
        self.failIf(self.nod_def < self.nod_test1)
        # self.failUnless(self.nod_test1 == self.nod_def)

if __name__ == '__main__':
    unittest.main()
