
from graph import Graph
from node import Node
from edge import Edge
from random import random


def read_header(fd):
    "Parse a .tsp file and return a dictionary with header data."

    converters = {'NAME': str, 'TYPE': str, 'COMMENT': str, 'DIMENSION': int,
                  'EDGE_WEIGHT_TYPE': str, 'EDGE_WEIGHT_FORMAT': str,
                  'EDGE_DATA_FORMAT': str, 'NODE_COORD_TYPE': str,
                  'DISPLAY_DATA_TYPE': str}
    sections = converters.keys()
    header = {}

    # Initialize header.
    for section in sections:
        header[section] = None

    fd.seek(0)
    for line in fd:
        data = line.split(':')
        firstword = data[0].strip()
        if firstword in sections:
            header[firstword] = converters[firstword](data[1].strip())

    return header


def read_nodes(header, fd, G):
    """
    Parse a .tsp file and return a dictionary of nodes, of the form
    {id:(x,y)}. If node coordinates are not given, an empty dictionary is
    returned. The actual number of nodes is in header['DIMENSION'].
    """

    node_coord_type = header['NODE_COORD_TYPE']
    display_data_type = header['DISPLAY_DATA_TYPE']
    if node_coord_type not in ['TWOD_COORDS', 'THREED_COORDS'] and \
            display_data_type not in ['COORDS_DISPLAY', 'TWOD_DISPLAY']:
        # Node coordinates are not given.
        for i in range(header['DIMENSION']):
            G.add_node(
                Node(
                    name='Noeud {0:d}'.format(i),
                    data=[
                        1000 *
                        random() //
                        1,
                        1000 *
                        random() //
                        1]))
        return

    dim = header['DIMENSION']
    fd.seek(0)
    k = 0
    display_data_section = False
    node_coord_section = False

    for line in fd:
        if line.strip() == "DISPLAY_DATA_SECTION":
            display_data_section = True
            continue
        elif line.strip() == "NODE_COORD_SECTION":
            node_coord_section = True
            continue

        if display_data_section:
            data = line.strip().split()
            G.add_node(Node('Node', data=map(float, data[1:])))
            k += 1
            if k >= dim:
                break
            continue

        elif node_coord_section:
            data = line.strip().split()
            G.add_node(Node('Node', data=map(float, data[1:])))
            k += 1
            if k >= dim:
                break
            continue

    return


def read_edges(header, fd, G):
    "Parse a .tsp file and return the collection of edges as a Python set."

    edges = set()
    edge_weight_format = header['EDGE_WEIGHT_FORMAT']
    known_edge_weight_formats = ['FULL_MATRIX', 'UPPER_ROW', 'LOWER_ROW',
                                 'UPPER_DIAG_ROW', 'LOWER_DIAG_ROW',
                                 'UPPER_COL', 'LOWER_COL', 'UPPER_DIAG_COL',
                                 'LOWER_DIAG_COL']
    if edge_weight_format not in known_edge_weight_formats:
        return edges

    dim = header['DIMENSION']

    def n_nodes_to_read(n):
        format = edge_weight_format
        if format == 'FULL_MATRIX':
            return dim
        if format in ['LOWER_DIAG_ROW', 'UPPER_DIAG_COL']:
            return n + 1
        if format in ['LOWER_DIAG_COL', 'UPPER_DIAG_ROW']:
            return dim - n
        if format in ['LOWER_ROW', 'UPPER_COL']:
            return n
        if format in ['LOWER_COL', 'UPPER_ROW']:
            return dim - n - 1

    fd.seek(0)
    edge_weight_section = False
    k = 0
    n_edges = 0
    i = 0
    n_to_read = n_nodes_to_read(k)

    for line in fd:
        if line.strip() == "EDGE_WEIGHT_SECTION":
            edge_weight_section = True
            continue

        if edge_weight_section:
            data = line.strip().split()
            n_data = len(data)

            start = 0

            while n_data > 0:

                # Number of items that we read on this line
                # for the current node.
                n_on_this_line = min(n_to_read, n_data)

                # Read edges.
                for j in xrange(start, start + n_on_this_line):
                    n_edges += 1
                    if edge_weight_format in [
                            'UPPER_ROW', 'LOWER_COL'] and (
                            k != i + k + 1):

                        e_data = [G.get_node(k), G.get_node(
                            i + k + 1), int(data[j])]
                        e = Edge(
                            name='E from {0:d} to {1:d}'.format(
                                k, i + k + 1), data=e_data)

                        G.add_edge(e)
                        G.add_to_dict(e)
                    elif edge_weight_format in ['UPPER_DIAG_ROW',
                                                'LOWER_DIAG_COL'] and (k != k + i):

                        e_data = [G.get_node(k), G.get_node(
                            i + k), int(data[j])]
                        e = Edge(
                            name='E from {0:d} to {1:d}'.format(
                                k, i + k), data=e_data)

                        G.add_edge(e)
                        G.add_to_dict(e)
                    elif edge_weight_format in ['UPPER_COL', 'LOWER_ROW'] and (i + k + 1 != k):

                        e_data = [G.get_node(i + k + 1),
                                  G.get_node(k), int(data[j])]
                        e = Edge(
                            name='E from {0:d} to {1:d}'.format(
                                i + k + 1, 1), data=e_data)

                        G.add_edge(e)
                        G.add_to_dict(e)
                    elif edge_weight_format in ['UPPER_DIAG_COL',
                                                'LOWER_DIAG_ROW'] and (i != k):

                        e_data = [G.get_node(i), G.get_node(k), int(data[j])]
                        e = Edge(
                            name='E from {0:d} to {1:d}'.format(
                                i, k), data=e_data)

                        G.add_edge(e)
                        G.add_to_dict(e)
                    elif edge_weight_format == 'FULL_MATRIX' and (k < i):

                        e_data = [G.get_node(k), G.get_node(i), int(data[j])]
                        e = Edge(
                            name='E from {0:d} to {1:d}'.format(
                                k, i), data=e_data)

                        G.add_edge(e)
                        G.add_to_dict(e)
                    i += 1

                # Update number of items remaining to be read.
                n_to_read -= n_on_this_line
                n_data -= n_on_this_line

                if n_to_read <= 0:
                    start += n_on_this_line
                    k += 1
                    i = 0
                    n_to_read = n_nodes_to_read(k)

                if k >= dim:
                    n_data = 0

            if k >= dim:
                break

    return edges


if __name__ == "__main__":

    import sys

    finstance = sys.argv[1]
    G = Graph()
    with open(finstance, "r") as fd:

        header = read_header(fd)
        print 'Header: ', header
        dim = header['DIMENSION']
        edge_weight_format = header['EDGE_WEIGHT_FORMAT']

        print "Reading nodes"
        nodes = read_nodes(header, fd, G)

        print "Reading edges"
        edges = read_edges(header, fd, G)

    #G.plot_graph()

    #print (G)
