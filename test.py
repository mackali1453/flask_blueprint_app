# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 19:40:26 2021

@author: melik
"""
#this is test script
import unittest
import distance

class test_flask(unittest.TestCase):
    
    def test_inside_mkad(self):
        # Addresses inside MKAD does not need to be calculated thus adresses below must be tested for that.
        self.assertEqual(float(distance.homepage("grand kremlin palace")),0)
        self.assertEqual(float(distance.homepage("red square")),0)
        self.assertEqual(float(distance.homepage("St. Basil's Cathedral")),0)
    def test_invalid_data(self):
        # Invalid input data test
        self.assertRaises(ValueError,distance.homepage,1.2)
    def test_outside_mkad(self):
        # Addresses outside MKAD must be more than zero to prove that the application runs properly.
        self.assertNotEqual(float(distance.homepage("istanbul")),0)
        self.assertNotEqual(float(distance.homepage("st. petersburg")),0)
        self.assertNotEqual(float(distance.homepage("ankara")),0)
if __name__ == "__main__":
    unittest.main() 