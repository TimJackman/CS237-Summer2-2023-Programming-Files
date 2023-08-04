OK_FORMAT = True

test = {   'name': 'kargersAlgorithm',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': '>>> G = nx.relabel_nodes(nx.MultiGraph(nx.complete_graph(5)), lambda x: colToLetter(x))\n'
                                               '>>> cut = kargersAlgorithm(G, np.random.default_rng(42))\n'
                                               '>>> assert nx.is_isomorphic(G,nx.complete_graph(5)), "It looks like you did not copy the graph!"\n'
                                               '>>> assert cut == ({\'C\'}, {\'D\', \'E\', \'A\', \'B\'}, 4), f"We ran your algorithm with seed 42 on the complete graph of 5 vertices and expected '
                                               '{({\'C\'}, {\'D\', \'E\', \'A\', \'B\'}, 4)} but got {cut}"\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
