'''
Created on 27 nov. 2017

@author: ClaudiaEstefania
'''
import unittest
from calc.Calculator import Calculator

class TestCalc(unittest.TestCase):
    
    def testAdd(self):
        calculator = Calculator()
        result = calculator.add(operanda=2, operandb=3)
        self.assertEqual(result, 5, "Addition failed")
    