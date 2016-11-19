from graph import Graph
from mst import Mst
# from random import randint
from wline import File
from opt_paths import Paths


class Cycle(Graph):
    """ This is a special kind of graph made to search for the shortest path"""

    # ordrerd_list = []
    file = File()

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
                source = original_graph.get_node(0).ancestor

            elif method == 'prim':
                # source = original_graph.get_node(randint(0, original_graph.get_nb_nodes() - 1))
                source = original_graph.get_node(num_node)
                self.__spanning_tree = Mst(
                    original_graph=original_graph,
                    method='prim',
                    heap=True,
                    source=source)

            self.add_to_list(source)
            self.trace_cycle(original_graph)
            # self.__spanning_tree.plot_graph()
            # self.plot_graph()
            # print self.__spanning_tree.get_neighbors(source).keys()
            try:
                self.poids_algo, self.poids_opt = self.weight, Paths.dico_opt_path[
                    name]
            except KeyError:
                self.poids_algo, self.poids_opt = self.weight, 99999999

            self.err_rel = ((1000 * (float(self.poids_algo) -
                                     float(self.poids_opt))) // float(self.poids_opt)) / 1000
            # print "Poids obtenu via l'algorithme de Rosenkrantz : " + str(self.poids_algo)
            # print "Poids optimal : " + str(self.poids_opt) + "\nErreur
            # relative : " + str(self.err_rel * 100) + "%"

    @property
    def spanning_tree(self):
        return self.__spanning_tree

    def add_to_list(self, node):
        # self.ordrerd_list.append(node)
        self.file.enqueue(node)
        # print "node = ", node
        local_node_neighbors = self.__spanning_tree.get_neighbors2(node)
        # print "local_neighbors == " , local_node_neighbors , '\n\n'
        while not (local_node_neighbors.is_empty()):
            local_node = local_node_neighbors.dequeue()
            if not (local_node in self.file):
                self.add_to_list(local_node)

    def trace_cycle(self, original_graph):
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
