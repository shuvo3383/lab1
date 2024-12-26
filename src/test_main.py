import unittest
from main import app

class PersonAPITestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_create_person(self):
        response = self.app.post('/api/v1/persons', json={'name': 'John Doe'})
        self.assertEqual(response.status_code, 201)
        self.assertIn('Location', response.headers)

    def test_list_persons(self):
        self.app.post('/api/v1/persons', json={'name': 'John Doe'})
        response = self.app.get('/api/v1/persons')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)

    def test_get_person(self):
        self.app.post('/api/v1/persons', json={'name': 'John Doe'})
        response = self.app.get('/api/v1/persons/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['name'], 'John Doe')

    def test_update_person(self):
        self.app.post('/api/v1/persons', json={'name': 'John Doe'})
        response = self.app.patch('/api/v1/persons/1', json={'name': 'Jane Doe'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['name'], 'Jane Doe')

    def test_delete_person(self):
        self.app.post('/api/v1/persons', json={'name': 'John Doe'})
        response = self.app.delete('/api/v1/persons/1')
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()
