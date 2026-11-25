
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

import unittest

class TestSentimenAnalyzer (unittest.TestCase):
    
    def test_sentiment_analyzer(self):
        result_1 = sentiment_analyzer("Adoro esta nueva tecnología.")["label"]
        self.assertEqual(result_1, "POSITIVE")
        result_2 = sentiment_analyzer("Odio python.")["label"]
        self.assertEqual(result_2 , "NEGATIVE")
        result_3 = sentiment_analyzer("Está regular, cumple su función sin más.")["label"]
        self.assertEqual(result_3, "NEUTRAL")
        
if __name__ == "__main__":
    unittest.main()
            
            