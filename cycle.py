from graph import Graph
from mst import Mst
# from random import randint
from wline import File
from opt_paths import Paths
from wline import Stack


class Cycle(Graph):
    """ This is a special kind of graph made to search for the shortest path"""

    # ordrerd_list = []
    file = File()
    __found = True
    __kruskal = False
    __prim = False

    def __init__(
            self,
            name='Sans nom',
            original_graph=None,
            method='kruskal',
            num_node=0):
        Graph.__init__(self, name)
        if original_graph is not None:
            source = original_graph.get_node(num_node)
            for node in original_graph.get_nodes():
                self.add_node(node)
            # print name
            if method == 'kruskal':
                self.__spanning_tree = Mst(
                    original_graph=original_graph, method='kruskal')
                self.__source = original_graph.get_node(0).ancestor
                self.__kruskal = True

            elif method == 'prim':
                # source = original_graph.get_node(randint(0, original_graph.get_nb_nodes() - 1))
                self.__source = original_graph.get_node(num_node)
                self.__spanning_tree = Mst(
                    original_graph=original_graph,
                    method='prim',
                    heap=True,
                    source=source)
                self.__prim = True
            # LIGNE A CHANGER SI ON VEUT PARCOURIR EN ITERATIF (OU EN RECURSIF)
            self.dfs(source)
            self.trace_cycle(original_graph)
            # self.__spanning_tree.plot_graph()
            # self.plot_graph()
            # print self.__spanning_tree.get_neighbors(source).keys()
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
