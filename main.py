from read_stsp import read_edges
from read_stsp import read_header
from read_stsp import read_nodes
from graph import Graph
from mst import Mst

if __name__ == "__main__":
    import sys

    finstance = sys.argv[1]
    G = Graph()
    with open(finstance, "r") as fd:
        header = read_header(fd)
        # print 'Header: ', header
        dim = header['DIMENSION']
        edge_weight_format = header['EDGE_WEIGHT_FORMAT']

        print "Reading nodes"
        nodes = read_nodes(header, fd, G)

        print "Reading edges"
        edges = read_edges(header, fd, G)

    # G.plot_graph()
    # print (G)

    kruskal_tree = Mst(original_graph=G, method='kruskal')

    # kruskal_tree.plot_graph()

    print 'Poids total du graphe : ' + header.__getitem__('NAME') + ' = ' + str(kruskal_tree.weight) + '\n'

    kruskal_tree2 = Mst(original_graph=G,method='prim')

    print 'Poids total du graphe 2 : ' + header.__getitem__('NAME') + ' = ' + str(kruskal_tree2.weight) + '\n'

    # kruskal_tree2.plot_graph()
