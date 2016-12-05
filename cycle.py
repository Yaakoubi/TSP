from graph import Graph
from mst import Mst
# from random import randint
from wline import File
from opt_paths import Paths
from wline import Stack
from node import Node
import random as rand
from edge import Edge


class Cycle(Graph):
    """ This is a special kind of graph made to search for the shortest path"""

    # ordrerd_list = []

    def __init__(
            self,
            name='Sans nom',
            original_graph=None,
            method='kruskal',
            num_node=0):
        self.file = File()
        self.__found = True
        self.__kruskal = False
        self.__prim = False
        Graph.__init__(self, name)
        if original_graph is not None:
            self.__source = original_graph.get_node(num_node)
            self.__source.reset_node_count()
            for node in original_graph.get_nodes():
                self.add_node(node)
            # print name
            if method == 'kruskal':
                self.__spanning_tree = Mst(
                    original_graph=original_graph, method='kruskal')
                self.__source = original_graph.get_node(0).ancestor
                self.__kruskal = True

            else :
                # source = original_graph.get_node(randint(0, original_graph.get_nb_nodes() - 1))
                self.__source = original_graph.get_node(num_node)
                self.__spanning_tree = Mst(
                    original_graph=original_graph,
                    method='prim',
                    heap=True,
                    source=self.__source)
                self.__prim = True
            # LIGNE A CHANGER SI ON VEUT PARCOURIR EN ITERATIF (OU EN RECURSIF)
            self.dfs_iterativ(self.__source)
            self.trace_cycle(original_graph)
            # self.__spanning_tree.plot_graph()
            # self.plot_graph()
            # print self.__spanning_tree.get_neighbors(self.__source).keys()
            try:
                self.poids_algo, self.poids_opt = self.weight, Paths.dico_opt_path[
                    name]
            except KeyError:
                self.__found = False
                self.poids_algo, self.poids_opt = self.weight, 99999999
            if self.__found:
                self.err_rel = ((1000 * (float(self.poids_algo) -
                                         float(self.poids_opt))) // float(self.poids_opt)) / 1000
            # print "Poids obtenu via l'algorithme de Rosenkrantz : " + str(self.poids_algo)
            # print "Poids optimal : " + str(self.poids_opt) + "\nErreur
            # relative : " + str(self.err_rel * 100) + "%"

    @property
    def spanning_tree(self):
        return self.__spanning_tree

    @property
    def source(self):
        return self.__source

    @property
    def found(self):
        return self.__found

    @property
    def kruskal(self):
        return self.__kruskal

    @property
    def prim(self):
        return self.__prim

    def dfs(self, node):
        # self.ordrerd_list.append(node)
        self.file.enqueue(node)
        # print "node = ", node
        local_node_neighbors = self.__spanning_tree.get_neighbors3(node)
        # print "local_neighbors == " , local_node_neighbors , '\n\n'
        while not (local_node_neighbors.is_empty()):
            local_node = local_node_neighbors.dequeue()
            if not (local_node in self.file):
                self.dfs(local_node)

    def dfs_iterativ(self, root):
        """version iterative du parcours en profondeur de l'arbre de source = root"""
        pile = Stack()
        pile.push(root)  # root devient racine d'une nouvelle arborescence.
        while not pile.is_empty():
            u = pile.pop()
            self.file.enqueue(u)
            neighbors = self.__spanning_tree.get_neighbors(u)
            # while not (neighbors.is_empty()):
            for neighbor in neighbors:
                # neighbor = neighbors.dequeue()
                if not (neighbor in self.file):
                    pile.push(neighbor)
        return

    def trace_cycle(self, original_graph):
        """build the cycle,once the nodes are in ordre"""
        # for i in xrange(0,original_graph.get_nb_nodes()):
        #     self.add_edge(original_graph.get_edge_from_dict(self.ordrerd_list[i-1],self.ordrerd_list[i]))
        source = self.file.dequeue()
        node2 = source
        while not self.file.is_empty():
            node1 = node2
            node2 = self.file.dequeue()
            edge_to_add = original_graph.get_edge_from_dict(node1, node2)
            self.add_edge(edge_to_add)
            self.add_weight(edge_to_add.weight)
        edge_to_add = original_graph.get_edge_from_dict(source, node2)
        self.add_edge(edge_to_add)
        self.add_weight(edge_to_add.weight)


if __name__ == '__main__':

    G = Graph(name='Graphe test')
    for k in range(10):  # nb_nodes ici = 10
        coords = [1000 * rand.random() // 1, 1000 * rand.random() // 1]
        test_node = Node(name='Ntest {0:d}'.format(k), data=coords)
        G.add_node(test_node)
    for i in range(G.get_nb_nodes()):
        for j in range(
                i):  # pas de redondance , donc nb_edges = nb_nodes * (nb_nodes-1) /2
            start = G.get_node(i)
            arrival = G.get_node(j)
            # print  start , arrival , '\n'
            e_data = [start, arrival, 200 * rand.random() // 1]
            e = Edge(
                name='Test Edge',
                data=e_data)
            G.add_edge(e)
            G.add_to_dict(e)

    # print G

    print G.get_edge_from_dict(G.get_node(3), G.get_node(6))
    print G.get_edge_from_dict(G.get_node(6), G.get_node(3))
    print G.get_edge_from_dict(G.get_node(6), G.get_node(6))

    cycle1 = Cycle(name="GrapheTest", original_graph=G, method='kruskal')
    print cycle1.source

    cycle1.dfs_iterativ(cycle1.source)
    cycle1.dfs_iterativ(cycle1.source)
    tree = cycle1.spanning_tree
