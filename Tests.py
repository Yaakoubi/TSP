""" Fichier de tests unitaires. """

from edge import Edge
from node import Node
from graph import Graph
import unittest
import random

edg_test = Edge("edge_test", 34)
edg_def = Edge()
nod_test =  Node("node_test", [34, 45, 79])
nod_def = Node()
gra_test = Graph("graph_test")
gra_def = Graph()


class TestEdgeMethods(unittest.TestCase):
    """ Teste les differentes fonctions de la classe Edge."""

    def test_get_name(self):
        """ Verification du nom renvoye par la fonction get_name. """
        self.assertEqual('Sans nom', edg_def.get_name())
        self.assertEqual('edge_test', edg_test.get_name())

    def test_get_id(self):
        """ Verification que l'indice d'une arete est un nombre entier. """
        self.assertTrue(type(edg_test.get_id()) is int)

    def test_get_data(self):
        """ Verification que la valeur par defaut d'une donnee est None et sinon qu'elle est un nombre entier. """
        self.assertEqual(edg_def.get_data(), None)
        self.assertTrue(type(edg_test.get_data()) is int)

    def test_repr(self):
        """ Verification qu'une chaine de caracteres est bien renvoyee a l'affichage par le module print. """
        edges = []
        edges.append(Edge())
        self.assertTrue(type(edges.__repr__()) is str)


class TestNodeMethods(unittest.TestCase):
    """ Teste les differentes fonctions de la classe Node."""

    def test_get_name(self):
        """ Verification du nom renvoye par la fonction get_name. """
        self.assertEqual('Sans nom', nod_def.get_name())
        self.assertEqual('node_test', nod_test.get_name())

    def test_get_id(self):
        """ Verification que l'indice d'une arete est un nombre entier. """
        self.assertTrue(type(nod_test.get_id()) is int)

    def test_get_data(self):
        """ Verification que la valeur par defaut d'une donnee est None et sinon qu'elle est un nombre entier. """
        self.assertEqual(nod_def.get_data(), None)
        self.assertTrue(type(nod_test.get_data()) is list)

    def test_repr(self):
        """ Verification qu'une chaine de caracteres est bien renvoyee a l'affichage par le module print. """
        nodes = []
        nodes.append(Node())
        self.assertTrue(type(nodes.__repr__()) is str)


class TestgraphMethods(unittest.TestCase):
    """ Teste les differentes fonctions de la classe Graph."""

    def test_get_name(self):
        """ Verification du nom renvoye par la fonction get_name. """
        default = Graph()
        graph_test = Graph("graph_test")
        self.assertEqual('Sans nom', default.get_name())
        self.assertEqual('graph_test', graph_test.get_name())

    def test_add_and_get_node(self):
        """ Verifie si les noeuds entres s'ajoutent en fin de liste et s'ils correspondent a un type Node """
        gra_test.add_node(nod_test)
        self.failUnless(gra_test.get_node(-1) == nod_test)
        self.failUnless(type(gra_test.get_node(-1)) is Node)

    def test_get_nodes(self):
        """Verifie si la liste de noeuds renvoie bien des objets de type noeuds et si ceux-ci sont bien ordonnes """
        gra_test.add_node(nod_test)
        self.failUnless(gra_test.get_nodes()[-1] == nod_test)

    def test_add_and_get_edges(self):
        """ Verifie si les aretes entrees s'ajoutent en fin de liste et si elles correspondent a un type Edge """
        gra_test.add_edge(edg_test)
        self.failUnless(gra_test.get_edges()[-1] == edg_test)
        self.failUnless(type(random.choice(gra_test.get_edges())) is Edge)

    def test_get_nb_edges_and_nodes(self):
        """ Verifie si le nombre de noeuds entres correspond bien a celui retourne par les fonctions """
        gra_test.add_edge(edg_test)
        self.assertEqual(gra_test.get_nb_edges(), len(gra_test.get_edges()))
        gra_test.add_node(nod_test)
        self.assertEqual(gra_test.get_nb_nodes(), len(gra_test.get_nodes()))

    def test_repr(self):
        """ Verification qu'une chaine de caracteres est bien renvoyee a l'affichage par le module print. """
        self.assertTrue(type(gra_test.__repr__()) is str)

###
    # def test_plot_graph(self):
    #     """ Je ne vois pas sur quoi faire un test... """
###


if __name__ == '__main__':
    print("hello")
    unittest.main()
