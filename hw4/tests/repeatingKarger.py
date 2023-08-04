OK_FORMAT = True

test = {   'name': 'repeatingKarger',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> def testnRunWithSeed11():\n'
                                               '...     K10 = nx.complete_graph(10)\n'
                                               '...     G = nx.MultiGraph(K10)\n'
                                               '...     nx.relabel_nodes(G, lambda x: colToLetter(x),copy=False)\n'
                                               "...     assert nRunKargersAlgorithm(G, 1, np.random.default_rng(11)) == ({'G', 'H', 'A', 'J', 'F', 'I', 'E', 'B'}, {'D', 'C'}, 16)\n"
                                               '...     assert nRunKargersAlgorithm(G, 10, np.random.default_rng(11))[2] == 9, f("We ran your nRunKargersAlgorithm 10 times on the complete graph on '
                                               '10 vertices with seed 11 and expected you to find a cut of 9")\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
