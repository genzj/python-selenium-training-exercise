import unittest

try:
    from unittest.mock import Mock, patch
except ImportError:
    from mock import Mock, patch

TODOS = [
  {
    "userId": 1,
    "id": 1,
    "title": "delectus aut autem",
    "completed": False
  },
  {
    "userId": 1,
    "id": 2,
    "title": "quis ut nam facilis et officia qui",
    "completed": False
  },
  {
    "userId": 1,
    "id": 3,
    "title": "fugiat veniam minus",
    "completed": False
  }
]

from api_client import read_todo

class TestApiRequest(unittest.TestCase):
    @patch('api_client.requests.get')
    def test_nok_response(self, mock_get):
        mock_get.return_value = Mock(ok=False)
        response = read_todo()
        self.assertEqual(response, [])

    @patch('api_client.requests.get')
    def test_ok_response(self, mock_get):
        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = TODOS
        response = read_todo()
        self.assertEqual(len(response), 3)
        self.assertEqual(response, TODOS)

    @patch('api_client.requests.get')
    def test_response_slice(self, mock_get):
        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = TODOS
        response = read_todo(1)
        self.assertEqual(len(response), 1)
        self.assertEqual(response, TODOS[:1])


if __name__ == '__main__':
    unittest.main()

