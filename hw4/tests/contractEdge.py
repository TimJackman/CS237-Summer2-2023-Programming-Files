OK_FORMAT = True

test = {   'name': 'contractEdge',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> G = nx.relabel_nodes(nx.MultiGraph(nx.complete_graph(3)), lambda x: colToLetter(x))\n'
                                               ">>> contractEdge(G, ('B','C'))\n"
                                               '>>> assert list(G.edges) == [(\'A\', \'B,C\', 0), (\'A\', \'B,C\', 1)], f"The graph G still has edges: {list(G.edges)} and not {[(\'A\', \'B,C\', 0), '
                                               '(\'A\', \'B,D\', 1)]} when we tried contracting (B,C) in the complete graph of three vertices" \n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
