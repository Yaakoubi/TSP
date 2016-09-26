from edge import Edge
from node import Node
from graph import Graph
import unittest
import random


class TestgraphMethods(unittest.TestCase):
    """ Teste les differentes fonctions de la classe Graph."""

    def setUp(self):
        """ Liste de commandes qui sera lancee a chaque test """
        self.gra_def = Graph()
        self.gra_test = Graph("graph_test")

        self.nod_test1 = Node("noeud_sans_nom1")
        self.nod_test2 = Node("noeud_sans_nom2")

        self.edg_test1 = Edge("arete_sans_nom1", [1,2,3])
        self.edg_test2 = Edge("arete_sans_nom2")
        self.edg_test3 = Edge("arete_sans_nom3", 3)
        self.edg_test4 = Edge("arete_sans_nom3", (1, 2, 3))
        self.edg_test5 = Edge("arete_sans_nom3", (3,"e",1))  # <-- Moyen, faire assertions pour empecher

        self.gra_test.add_node(self.nod_test1)
        self.gra_test.add_node(self.nod_test2)
        self.gra_test.add_edge(self.edg_test1)
        self.gra_test.add_edge(self.edg_test2)



    def test_get_name(self):
        """ Verification du nom renvoye par la fonction get_name. """
        self.assertEqual('Sans nom', self.gra_def.get_name())
        self.assertEqual('graph_test', self.gra_test.get_name())

    def test_add_and_get_node(self):
        """ Verifie si les noeuds entres s'ajoutent en fin de liste et s'ils correspondent a un type Node """
        self.failUnless(self.gra_test.get_node(-1) == self.nod_test2)
        self.assertRaises(AssertionError,self.gra_test.add_node, "Ceci n'est pas un noeud")

    def test_get_nodes(self):
        """Verifie si la liste de noeuds renvoie bien des objets de type noeuds et si ceux-ci sont bien ordonnes """
        self.failUnless(self.gra_test.get_nodes()[-1] == self.nod_test2)
        self.assertEqual(len(self.gra_test.get_nodes()),2)

    def test_add_and_get_edges(self):
        """ Verifie si les aretes entrees s'ajoutent en fin de liste et si elles correspondent a un type Edge """
        self.failUnless(self.gra_test.get_edges()[-1] == self.edg_test2)
        self.assertRaises(AssertionError, self.gra_test.add_edge, "Ceci n'est pas une arete")

    def test_get_nb_edges_and_nodes(self):
        """ Verifie si le nombre de noeuds entres correspond bien a celui retourne par les fonctions """
        self.assertEqual(self.gra_test.get_nb_edges(), len(self.gra_test.get_edges()))
        self.assertEqual(self.gra_test.get_nb_nodes(), len(self.gra_test.get_nodes()))

    def test_add_to_dict(self):
        """ Verifie le bon fonctionnement du dictionnaire : la fonction marche quand
        un edge dispose d'une liste (ou tuple ou str) en donnees et met une erreur sinon"""
        self.assertEqual(self.gra_test.add_to_dict(self.edg_test1), None)
        self.assertRaises(TypeError,self.gra_test.add_to_dict, self.edg_test2)
        self.assertRaises(TypeError,self.gra_test.add_to_dict, self.edg_test3)
        self.assertEqual(self.gra_test.add_to_dict(self.edg_test4), None)
        self.assertEqual(self.gra_test.add_to_dict(self.edg_test5), None)

    # A FINIR !!!!
    def test_get_edge_id_from_dict(self):
        """ Verifie le bon fonctionnement de la fonction get_edge_id_from_dict """
        self.gra_test.add_to_dict(self.edg_test1)
        self.gra_test.add_to_dict(self.edg_test4)
        # self.gra_test.add_to_dict(self.edg_test5)

        self.gra_test.get_edge_id_from_dict(1, 4)
        self.gra_test.get_edge_id_from_dict(1, 1)
        self.gra_test.get_edge_id_from_dict(1, -1)
        self.gra_test.get_edge_id_from_dict(4, 1)

    # A FINIR !!!!!
    def test_get_edge_from_dict(self):
        """ Verifie le bon fonctionnement de la fonction get_edge_from_dict """
        self.gra_test.add_to_dict(self.edg_test1)
        self.gra_test.add_to_dict(self.edg_test4)
        # self.gra_test.add_to_dict(self.edg_test5)

        self.gra_test.get_edge_from_dict(1, 4)
        self.gra_test.get_edge_from_dict(1, 1)
        self.gra_test.get_edge_from_dict(1, -1)
        self.gra_test.get_edge_from_dict(4, 1)

    def test_repr(self):
        """ Verification qu'une chaine de caracteres est bien renvoyee a l'affichage par le module print. """
        self.assertTrue(type(self.gra_test.__repr__()) is str)



if __name__ == '__main__':
    unittest.main()