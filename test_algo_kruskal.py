from read_stsp import read_edges
from read_stsp import read_header
from read_stsp import read_nodes

from mst import Mst


if __name__ == "__main__":

    import sys

    finstance = sys.argv[1]
    G = Mst()
    with open(finstance, "r") as fd:

        header = read_header(fd)
        print 'Header: ', header
        dim = header['DIMENSION']
        edge_weight_format = header['EDGE_WEIGHT_FORMAT']

        print "Reading nodes"
        nodes = read_nodes(header, fd, G)

        print "Reading edges"
        edges = read_edges(header, fd, G)

    # G.plot_graph()
    # print (G)

    G_arb = Mst(original_graph=G)

    G_arb.plot_graph()
