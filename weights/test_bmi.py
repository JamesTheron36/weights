#!/usr/bin/env python3
import unittest
import bmi

class test_bmi(unittest.TestCase):

    def test_ounces2Pounds(self):
        n = bmi.ounces2pounds(10)
        self.assertEqual(n,0.625)

    def test_stones2pounds(self):
        n = bmi.stones2pounds(10)
        self.assertEqual(n,140)

    def test_wegiht2kg(self):
        n = bmi.weight2kg(10,10,10)
        self.assertEqual(n,140.909)

    def test_height2metres(self):
        n = bmi.height2metres(5, 8)
        self.assertEqual(n,1.768)

    def test_categorise(self):
        n = bmi.categorise(70, 1.76)
        self.assertEqual(n, 'B')
        a = bmi.categorise(60, 1.8)
        self.assertEqual(a, 'A')
        b = bmi.categorise(88, 1.8)
        self.assertEqual(b, 'C')
        c = bmi.categorise(95, 1.45)
        self.assertEqual(c, 'D')



