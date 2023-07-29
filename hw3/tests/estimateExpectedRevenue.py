OK_FORMAT = True

test = {   'name': 'estimateExpectedRevenue',
    'points': 1,
    'suites': [   {   'cases': [   {'code': '>>> assert abs(estimateExpectedRevenue(1,100,30,1,42)- 39.71764207664884) < 0.0001\n', 'hidden': False, 'locked': False},
                                   {'code': '>>> assert (estimateExpectedRevenue(10,100,30,1,42) - 89.62854441860848) < 0.0001\n', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
