# Testing taxonomies: https://wiki.python.org/moin/PythonTestingToolsTaxonomy

# unittest is a testing module for Python
# Python unittest reference: https://docs.python.org/3/library/unittest.html

import unittest

from moo import moo

# Test whether moo(0) returns an empty string as desired
# The output has to be returned (see moo.py)
class Test_moo(unittest.TestCase):
	def test0(self):
		self.assertEqual(moo(0), "")
	def test1(self):
		self.assertEqual(moo(1), "moo ")
	def test2(self):
		self.assertEqual(moo(2), "moo moo ")
		
unittest.main()