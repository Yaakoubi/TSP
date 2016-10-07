from read_stsp import read_edges
from read_stsp import read_header
from read_stsp import read_nodes
from graph import Graph


def find_parent(edge_start):
    if parent[edge_start] != edge_start:
        parent[edge_start] = find_parent(parent[edge_start])
    return parent[edge_start]



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

    # G.plot_graph()
    #print (G)

    G_arb = Graph()
    parent = {}
    arborescence = []
    for node in G.get_nodes():
        G_arb.add_node(node)
        parent[node.get_id()] = node.get_id()

    list_edges = G.get_edges()
    ordered_weight_list = []
    for edge in list_edges:
        weight, edge = edge.weight, edge
        ordered_weight_list.append((weight,edge))
    ordered_weight_list.sort()

    first_edge = True
    for weight, edge in ordered_weight_list:
        # print parent[edge.end.get_id()]
        if first_edge:
            if edge.end.get_id() < edge.start.get_id() :
                parent[edge.start.get_id()] = edge.end.get_id()
            else:
                parent[edge.end.get_id()] = edge.start.get_id()
            arborescence.append(edge)
            first_edge = False
            continue
        if find_parent(edge.start.get_id()) != find_parent(edge.end.get_id()):
            if find_parent(edge.start.get_id()) < find_parent(edge.end.get_id()):
                parent[find_parent(edge.end.get_id())] = edge.start.get_id()
            else:
                parent[find_parent(edge.start.get_id())] = edge.end.get_id()
            arborescence.append(edge)

    for edge in arborescence :
        G_arb.add_edge(edge)

    G_arb.plot_graph()
