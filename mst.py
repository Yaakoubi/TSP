from graph import Graph


class Mst(Graph):
    """ This is a special king of graph made to perform Kruskal Algorithm"""

    def __init__(self, name='Sans nom', original_graph=None):
        Graph.__init__(self, name)
        if original_graph is not None:
            self.kruskal(original_graph)

    def kruskal(self, original_graph=None):
        """sets the tree using the Kruskal algorithm """
        if (not isinstance(original_graph, Graph)) or (original_graph is None):
            return 0
        if (self.get_nb_nodes() > 0) or (self.get_nb_edges() > 0):
            Graph.__init__(self, self.get_name())
        for node in original_graph.get_nodes():
            self.add_node(node)
        list_edges = sorted(original_graph.get_edges(), key=lambda i: i.weight)
        nb_nodes_mst, nb_nodes_original_graph = 1, original_graph.get_nb_edges()
        for edge in list_edges:
            # print (edge)
            if nb_nodes_mst < nb_nodes_original_graph and edge.start.ancestor != edge.end.ancestor:
                # print ('start anc :' +
                #       str(edge.start.ancestor.get_id()) +
                #       ' end anc : ' +
                #       str(edge.end.ancestor.get_id()))
                if edge.start.ancestor != edge.end.ancestor:
                    edge.end.ancestor.father = edge.start.ancestor
                    nb_nodes_mst += 1
                    self.add_edge(edge)
                    self.add_weight(edge.weight)
            elif nb_nodes_mst == nb_nodes_original_graph:
                print "OK, tous les noeuds sont pris!!"
                break
