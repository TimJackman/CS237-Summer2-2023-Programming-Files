OK_FORMAT = True

test = {   'name': 'generateTicketSamples',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> sample = generateTicketSamples(100,10)\n'
                                               '>>> \n'
                                               '>>> assert len(sample) == 100\n'
                                               '>>> assert (sample <= 10).all()\n'
                                               '>>> assert (sample).all()\n'
                                               '>>> assert all(sample[i] <= sample[i+1] for i in range(len(sample) - 1))\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
