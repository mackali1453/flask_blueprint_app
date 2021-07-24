# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 19:40:26 2021

@author: melik
"""
import unittest
import distance

class test_flask(unittest.TestCase):
    
    def test_inside_mkad(self):
        
        self.assertEqual(float(distance.homepage("grand kremlin palace")),0)
        self.assertEqual(float(distance.homepage("red square")),0)
        self.assertEqual(float(distance.homepage("St. Basil's Cathedral")),0)
    def test_invalid_data(self):
        self.assertRaises(ValueError,distance.homepage,1.2)
    def test_outside_mkad(self):
        self.assertNotEqual(float(distance.homepage("istanbul")),0)
        self.assertNotEqual(float(distance.homepage("st. petersburg")),0)
        self.assertNotEqual(float(distance.homepage("ankara")),0)
if __name__ == "__main__":
    unittest.main() 