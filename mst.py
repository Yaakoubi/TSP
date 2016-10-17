from graph import Graph


class Mst(Graph):
    """ This is a special king of graph made to perform Kruskal Algorithm"""

    def __init__(self, name='Sans nom', original_graph=None):
        Graph.__init__(self, name)
        self.__total_weight = 0
        if original_graph is not None:
            self.set_mst(original_graph)

    @property
    def weight(self):
        return self.__total_weight

    def set_mst(self, original_graph=None):
        """sets the tree using the Kruskal algorithm """
        if (not isinstance(original_graph, Graph)) or (original_graph is None):
            return 0
        for node in original_graph.get_nodes():
            self.add_node(node)

        list_edges = original_graph.get_edges()
        ordered_weight_list = []
        for edge in list_edges:
            weight, edge = edge.weight, edge
            ordered_weight_list.append((weight, edge))
        ordered_weight_list.sort()

        nb_nodes_mst, nb_nodes_original_graph = 1, len(
            original_graph.get_nodes())
        for weight, edge in ordered_weight_list:
            # print (edge)
            if nb_nodes_mst < nb_nodes_original_graph:
                if edge.start.ancestor != edge.end.ancestor:
                    # print ('start anc :' +
                    #       str(edge.start.ancestor.get_id()) +
                    #       ' end anc : ' +
                    #       str(edge.end.ancestor.get_id()))

                    if edge.start.ancestor == edge.start:
                        edge.start.father = edge.end
                        self.add_edge(edge)
                        nb_nodes_mst += 1
                        self.__total_weight += weight
                    elif edge.end.ancestor == edge.end:
                        edge.end.father = edge.start
                        self.add_edge(edge)
                        nb_nodes_mst += 1
                        self.__total_weight += weight
                    else:
                        edge.start.ancestor.father = edge.end
                        self.add_edge(edge)
                        nb_nodes_mst += 1
                        self.__total_weight += weight

                        # if edge.start.ancestor < edge.end.ancestor
                        #    edge.end.father.father = edge.start
                        # else:
                        #    edge.start.ancestor.father = edge.end.ancestor
            if nb_nodes_mst == nb_nodes_original_graph:
                print "OK, tous les noeuds sont pris!!"
                break
