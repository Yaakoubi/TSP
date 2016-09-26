import numpy as np
from read_stsp import *
from graph import Graph
from node import Node
from edge import Edge
from random import random


if __name__ == "__main__":

    import sys

    finstance = sys.argv[1]
    G = Graph ()
    with open(finstance, "r") as fd:

        header = read_header(fd)
        print 'Header: ', header
        dim = header['DIMENSION']
        edge_weight_format = header['EDGE_WEIGHT_FORMAT']

        print "Reading nodes"
        nodes = read_nodes(header, fd,G)


        print "Reading edges"
        edges = read_edges(header, fd,G)



    #G.plot_graph()

    print ( G )