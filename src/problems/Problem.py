# -*- coding: utf-8 -*-

'''
The Problem class defines the basic class for various problems.
The class has the following members:

Methods:
    __init__()
    get_info()

Variables:
    problem_type: specify the problem type
'''

class Problem:
    
    def __init__(self):
        # the default value is None
        self.problem_type = None
    
    def get_info(self):
        print('The problem is not specified.')