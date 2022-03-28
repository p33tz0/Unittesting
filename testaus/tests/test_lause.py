#Test that the lause.py file works as intended
import unittest
import testaus.lause.lause as lause

#Test that tests capitalize_first_letter function
class TestCapitalizeFirstLetter(unittest.TestCase):
    def test_capitalize_first_letter(self):
        sentence = "hello world"
        expected_result = "Hello world"
        result = lause.capitalize_first_letter(sentence)
        self.assertEqual(result, expected_result)
        
        
#TEst that tests check_punctuation function
class TestCheckPunctuation(unittest.TestCase):
    def test_check_punctuation(self):
        sentence = "hello world"
        expected_result = "hello world."
        result = lause.check_punctuation(sentence)
        self.assertEqual(result, expected_result)
        
#Test that tests capitalize function
class TestCapitalize(unittest.TestCase):
    def test_capitalize(self):
        word = "ei"
        expected_result = "EI"
        result = lause.capitalize(word)
        self.assertEqual(result, expected_result)
        
#Test that tests reverse_word function
class TestReverseWord(unittest.TestCase):
    def test_reverse_word(self):
        word = "kissa"
        expected_result = "assik"
        result = lause.reverse_word(word)
        self.assertEqual(result, expected_result)

#Test that tests lause.py file works as intended
class TestRunSentence(unittest.TestCase):
    def testrunsentence(self):
        sentence = "kissa on kalja"
        expected_result = "Assik ON ajlak."
        result = lause.run_sentence(sentence)
        self.assertEqual(result, expected_result)
        

        
if __name__ == '__main__':
    unittest.main()