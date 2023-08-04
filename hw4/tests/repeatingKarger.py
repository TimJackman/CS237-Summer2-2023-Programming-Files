OK_FORMAT = True

test = {   'name': 'repeatingKarger',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> G = nx.relabel_nodes(nx.MultiGraph(nx.complete_graph(10)), lambda x: colToLetter(x))\n'
                                               ">>> assert nRunKargersAlgorithm(G, 1, np.random.default_rng(11)) == ({'J', 'A', 'H', 'B', 'G', 'I', 'E', 'F'}, {'C', 'D'}, 16)\n"
                                               '>>> assert nRunKargersAlgorithm(G, 10, np.random.default_rng(11))[2] == 9, "We ran your nRunKargersAlgorithm 10 times on the complete graph on 10 '
                                               'vertices with seed 11 and expected you to find a cut of 9"\n',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': '>>> \n', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
