rm -r htmlcov/
coverage erase
coverage run -a test_edge.py
coverage run -a test_node.py
coverage run -a test_graph.py
coverage report -m graph.py edge.py node.py read_stsp.py test_edge.py test_node.py test_graph.py
coverage html graph.py edge.py node.py read_stsp.py test_edge.py test_node.py test_graph.py






rm -r htmlcov/
coverage erase
coverage run -a edge.py
coverage run -a graph.py
coverage run -a node.py
coverage run -a test_edge.py
coverage run -a test_node.py
coverage run -a test_graph.py
coverage run -a read_stsp.py instances/instances/stsp/bayg29.tsp 
coverage run -a read_stsp.py instances/instances/stsp/dantzig42.tsp 
coverage run -a read_stsp.py instances/instances/stsp/gr21.tsp 
coverage run -a read_stsp.py instances/instances/stsp/pa561.tsp 
coverage run -a read_stsp.py instances/instances/stsp/bays29.tsp 
coverage run -a read_stsp.py instances/instances/stsp/fri26.tsp 
coverage run -a read_stsp.py instances/instances/stsp/gr24.tsp 
coverage run -a read_stsp.py instances/instances/stsp/swiss42.tsp 
coverage run -a read_stsp.py instances/instances/stsp/brazil58.tsp 
coverage run -a read_stsp.py instances/instances/stsp/gr120.tsp 
coverage run -a read_stsp.py instances/instances/stsp/gr48.tsp 
coverage run -a read_stsp.py instances/instances/stsp/Test_full_matrix.tsp 
coverage run -a read_stsp.py instances/instances/stsp/brg180.tsp 
coverage run -a read_stsp.py instances/instances/stsp/gr17.tsp 
coverage run -a read_stsp.py instances/instances/stsp/hk48.tsp 
coverage run -a read_stsp.py instances/instances/stsp/Test_lower_diag_row.tsp
coverage run -a read_stsp.py instances/instances/stsp/Test_lower_row.tsp
coverage run -a read_stsp.py instances/instances/stsp/Test_upper_diag_row.tsp

coverage run -a test_read_stsp.py instances/instances/stsp/Test_lower_row.tsp
coverage run -a test_read_stsp.py instances/instances/stsp/Test_upper_diag_row.tsp
coverage run -a main.py instances/instances/stsp/bayg29.tsp 
coverage run -a main.py instances/instances/stsp/dantzig42.tsp 
coverage run -a main.py instances/instances/stsp/gr21.tsp 
coverage run -a main.py instances/instances/stsp/pa561.tsp 
coverage run -a main.py instances/instances/stsp/bays29.tsp 
coverage run -a main.py instances/instances/stsp/fri26.tsp 
coverage run -a main.py instances/instances/stsp/gr24.tsp 
coverage run -a main.py instances/instances/stsp/swiss42.tsp 
coverage run -a main.py instances/instances/stsp/brazil58.tsp 
coverage run -a main.py instances/instances/stsp/gr120.tsp 
coverage run -a main.py instances/instances/stsp/gr48.tsp 
coverage run -a main.py instances/instances/stsp/brg180.tsp 
coverage run -a main.py instances/instances/stsp/gr17.tsp 
coverage run -a main.py instances/instances/stsp/hk48.tsp 
coverage run -a main.py instances/instances/stsp/Test_full_matrix.tsp 
coverage run -a main.py instances/instances/stsp/Test_lower_diag_row.tsp
coverage run -a main.py instances/instances/stsp/Test_lower_row.tsp
coverage run -a main.py instances/instances/stsp/Test_upper_diag_row.tsp
coverage report -m node.py main.py mst.py graph.py edge.py test_read_stsp.py read_stsp.py test_edge.py  test_node.py test_graph.py 
coverage html node.py main.py mst.py graph.py edge.py test_read_stsp.py read_stsp.py test_edge.py  test_node.py test_graph.py 
