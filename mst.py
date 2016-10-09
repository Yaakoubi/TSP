from graph import Graph


class Mst(Graph):
    """ This is a special king of graph made to perform Kruskal Algorithm"""

    def __init__(self, name='Sans nom', original_graph=None):
        Graph.__init__(self, name)
        if original_graph is not None:
            self.set_mst(original_graph)

    def set_mst(self, original_graph=None):
        """sets the tree using the Kruskal algorithm """

        assert (isinstance(original_graph, Graph))
        for node in original_graph.get_nodes():
            self.add_node(node)

        list_edges = original_graph.get_edges()
        ordered_weight_list = []
        for edge in list_edges:
            weight, edge = edge.weight, edge
            ordered_weight_list.append((weight, edge))
        ordered_weight_list.sort()
        total_weight = 0

        for weight, edge in ordered_weight_list:
            # print (edge)
            if edge.start.ancestor != edge.end.ancestor:
                # print ('start anc :' +
                #       str(edge.start.ancestor.get_id()) +
                #       ' end anc : ' +
                #       str(edge.end.ancestor.get_id()))

                if edge.start.ancestor == edge.start:
                    edge.start.father = edge.end
                    self.add_edge(edge)
                    total_weight += weight
                elif edge.end.ancestor == edge.end:
                    edge.end.father = edge.start
                    self.add_edge(edge)
                    total_weight += weight
                else:
                    edge.start.ancestor.father = edge.end
                    self.add_edge(edge)
                    total_weight += weight

                    # if edge.start.ancestor < edge.end.ancestor
                    #    edge.end.father.father = edge.start
                    # else:
                    #    edge.start.ancestor.father = edge.end.ancestor

        print (original_graph.get_edges().__len__())
        print (total_weight)
