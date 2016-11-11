from graph import Graph
from wline import Queue
from wline import Heap


# from binary_tree import BinaryTree


class Mst(Graph):
    """ This is a special kind of graph made to perform Kruskal Algorithm"""

    def __init__(
            self,
            name='Sans nom',
            original_graph=None,
            method='kruskal',
            heap=False):
        Graph.__init__(self, name)
        if original_graph is not None:
            if method == 'kruskal':
                self.kruskal(original_graph)
            elif method == 'prim':
                self.prim(original_graph, heap)
                # self.kruskal_CompressionDesChemins(original_graph)

    def kruskal(self, original_graph=None):
        """Set the tree using the Kruskal algorithm
        make path in the tree by the ranking union method
        make a paths compression by the paths compression method"""

        if (not isinstance(original_graph, Graph)) or (original_graph is None):
            return 0
        if (self.get_nb_nodes() > 0) or (self.get_nb_edges() > 0):
            Graph.__init__(self, self.get_name())
        for node in original_graph.get_nodes():
            self.add_node(node)
        list_edges = sorted(original_graph.get_edges(), key=lambda i: i.weight)
        nb_nodes_mst, nb_nodes_original_graph = 1, original_graph.get_nb_nodes()
        for edge in list_edges:
            if nb_nodes_mst < nb_nodes_original_graph and edge.start.ancestor != edge.end.ancestor:
                if edge.end.ancestor.rank > edge.start.ancestor.rank:
                    edge.start.ancestor.father = edge.end.ancestor
                elif edge.end.ancestor.rank < edge.start.ancestor.rank:
                    edge.end.ancestor.father = edge.start.ancestor
                else:
                    edge.start.ancestor.rank += 1
                    edge.end.ancestor.father = edge.start.ancestor
                nb_nodes_mst += 1
                self.add_edge(edge)
                self.add_weight(edge.weight)

            elif nb_nodes_mst == nb_nodes_original_graph:
                # repr only : return node + rank then nb_time node is an
                # ancestor to be sure it's all OK
                # print "\nOK, tous les noeuds sont pris!!\n"
                # occurence = {}
                # for node in self.get_nodes():
                #     print "Noeud ", node, "rang", node.rank
                #     if node.father not in occurence:
                #         occurence[node.father] = 1
                #     else:
                #         occurence[node.father] += 1
                # print "\n\n     *** [Noeud] : [nombre de noeuds dont il est ancetre] ***\n"
                # for (key,item) in (occurence.items()):
                #     print key, ":", item
                break

    def prim(self, original_graph=None, heap=False):
        """Set the tree using the prim algorithm"""
        if (not isinstance(original_graph, Graph)) or (original_graph is None):
            return 0
        if (self.get_nb_nodes() > 0) or (self.get_nb_edges() > 0):
            Graph.__init__(self, self.get_name())
        for node in original_graph.get_nodes():
            self.add_node(node)

        nb_nodes_mst, nb_nodes_original_graph = 1, original_graph.get_nb_nodes()

        self.get_node(0).min_weight = 0

        if heap:
            queue = Heap()
        else:
            queue = Queue()

        for n in self.get_nodes():
            queue.enqueue(n)

        while not queue.is_empty():
            node1 = queue.dequeue()
            for node2 in self.get_nodes():
                edge = original_graph.get_edge_from_dict(node1, node2)
                if (node2 in queue) and (edge.weight < node2.min_weight):
                    node2.prim_father = node1
                    node2.min_weight = edge.weight
                    if heap:
                        queue.enqueue(node2)

        for node in self.get_nodes():
            if node.prim_father is not None:
                edge = original_graph.get_edge_from_dict(
                    node, node.prim_father)
                nb_nodes_mst += 1
                self.add_edge(edge)
                self.add_weight(edge.weight)
            if nb_nodes_mst == nb_nodes_original_graph:
                break
