import unittest
from unittest import TestSuite, loader 
from .routes_tests import rider_routes_test

test_cases = [

]

if __name__ == '__main__':
    suite = TestSuite()
    for test in test_cases:
        tests = loader.loadTestsFromModule(test)
        suite.addTests(tests)
    unittest.main()