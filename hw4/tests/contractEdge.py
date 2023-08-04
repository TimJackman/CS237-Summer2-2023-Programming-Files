OK_FORMAT = True

test = {   'name': 'contractEdge',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> def testK3ContractBC():\n'
                                               '...     K3 = nx.complete_graph(3)\n'
                                               '...     G = nx.MultiGraph(K3)\n'
                                               '...     nx.relabel_nodes(G, lambda x: colToLetter(x),copy=False)\n'
                                               "...     contractEdge(G, ('B','C'))\n"
                                               '...     assert list(G.edges) == [(\'A\', \'B,C\', 0), (\'A\', \'B,C\', 1)], f"Your code output: {list(G.edges)} and not {[(\'A\', \'B,C\', 0), (\'A\', '
                                               '\'B,D\', 1)]}" \n'
                                               '>>> \n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
