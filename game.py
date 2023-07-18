OK_FORMAT = True

test = {   'name': 'game',
    'points': 1.5,
    'suites': [   {   'cases': [   {'code': '>>> \n>>> assert game(["B"],"BBR") == "tie"\n>>> \n', 'hidden': False, 'locked': False},
                                   {'code': '>>> assert game(["B","B","R"],"BBR") == "win"\n>>> \n', 'hidden': False, 'locked': False},
                                   {'code': '>>> assert game(["B","B","R"],"BRB") == "lose"\n>>> \n>>> \n', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
