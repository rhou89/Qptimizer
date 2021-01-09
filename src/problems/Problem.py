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

import sys
class Problem:
    
    def __init__(self):
        # the default value is None
        self.problem_type = None
    
    def get_info(self):
        print('The problem is not specified.')
    
    def checkAllInt(self, items):
        for item in items:
            if type(item) != int:
                sys.exit('Invalid input(s): int expected.')
        return items
    
    def checkNum(self, item):
        if type(item) not in [int, float]:
            sys.exit('Invalid input(s): number expected.')
        return item
    
    def display(self, info):
        print('='*40, info, '='*40)