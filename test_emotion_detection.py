import unittest
from unittest.mock import patch, Mock
from emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):

    @patch("emotion_detection.requests.post")
    def test_emotion_detector(self, mock_post):
        mock_response = Mock()

        mock_response.json.return_value = {
            "emotionPredictions": [
                {
                    "emotion": {
                        "anger": 0.01,
                        "disgust": 0.02,
                        "fear": 0.03,
                        "joy": 0.90,
                        "sadness": 0.04
                    }
                }
            ]
        }

        mock_post.return_value = mock_response

        result = emotion_detector("I love this technology.")

        self.assertEqual(result["dominant_emotion"], "joy")
        self.assertEqual(result["anger"], 0.01)
        self.assertEqual(result["disgust"], 0.02)
        self.assertEqual(result["fear"], 0.03)
        self.assertEqual(result["joy"], 0.90)
        self.assertEqual(result["sadness"], 0.04)


if __name__ == "__main__":
    unittest.main()
