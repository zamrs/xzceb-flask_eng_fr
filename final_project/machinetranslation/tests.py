import unittest
from translator import englishToFrench, frenchToEnglish

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(englishToFrench(None), None) # test for null input
        self.assertEqual(englishToFrench('Hello'), 'Bonjour') # test for translation of 'Hello'

class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(frenchToEnglish(None), None) # test for null input
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello') # test for translation of 'Bonjour'