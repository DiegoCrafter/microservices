# services/users/project/tests/test_users.py
import json
import unittest
from project.tests.base import BaseTestCase
from project.tests.utils import add_user


class TestUserService(BaseTestCase):
    """Tests para el servicio Users."""
<<<<<<< HEAD
    def test_teachers(self):
=======
    def test_users(self):
>>>>>>> 56ca3da6228634e582d203ac043c663a48e90ac1
        """Asegurando que la ruta /ping  se comporta correctamente."""
        response = self.client.get('/users/ping')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('pong!', data['message'])
        self.assertIn('success', data['status'])

<<<<<<< HEAD
    def test_add_teacher(self):
=======
    def test_add_user(self):
        """Puede ser agregado"""
>>>>>>> 56ca3da6228634e582d203ac043c663a48e90ac1
        with self.client:
            response = self.client.post(
                '/users',
                data=json.dumps({
                    'username': 'diego',
<<<<<<< HEAD
                    'email': 'diego@upeu.edu.pe',
                    'password': 'greaterthaneight'
=======
                    'email': 'diego@upeu.edu.pe'
>>>>>>> 56ca3da6228634e582d203ac043c663a48e90ac1
                }),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 201)
            self.assertIn(
                'diego@upeu.edu.pe was added', data['message'])
            self.assertIn('success', data['status'])

<<<<<<< HEAD
    def test_add_teacher_invalid_json(self):
=======
    def test_add_user_invalid_json(self):
>>>>>>> 56ca3da6228634e582d203ac043c663a48e90ac1
        with self.client:
            response = self.client.post(
                '/users',
                data=json.dumps(()),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn('Invalid payload', data['message'])
            self.assertIn('fail', data['status'])

<<<<<<< HEAD
    def test_add_teacher_invalid_json_keys(self):
=======
    def test_add_user_invalid_json_keys(self):
>>>>>>> 56ca3da6228634e582d203ac043c663a48e90ac1
        with self.client:
            response = self.client.post(
                '/users',
                data=json.dumps({'email': 'diego.huarcaya@upeu.edu.pe'}),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn('Invalid payload', data['message'])
            self.assertIn('fail', data['status'])

<<<<<<< HEAD
    def test_add_teacher_duplicate_email(self):
=======
    def test_add_user_duplicate_email(self):
>>>>>>> 56ca3da6228634e582d203ac043c663a48e90ac1
        with self.client:
            self.client.post(
                '/users',
                data=json.dumps({
                    'username': 'diego',
<<<<<<< HEAD
                    'email': 'diegocrafter@upeu.edu.pe',
                    'password': 'greaterthaneight'
=======
                    'email': 'diegocrafter@upeu.edu.pe'
>>>>>>> 56ca3da6228634e582d203ac043c663a48e90ac1
                }),
                content_type='application/json',
            )
            response = self.client.post(
                '/users',
                data=json.dumps({
                    'username': 'diego',
<<<<<<< HEAD
                    'email': 'diegocrafter@upeu.edu.pe',
                    'password': 'greaterthaneight'
=======
                    'email': 'diegocrafter@upeu.edu.pe'
>>>>>>> 56ca3da6228634e582d203ac043c663a48e90ac1
                }),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn('That mail already exists', data['message'])
            self.assertIn('fail', data['status'])

<<<<<<< HEAD
    def test_single_teacher(self):
        user = add_user('diego', 'diegohuarcaya@upeu.edu.pe', 'greaterthaneight')
=======
    def test_single_user(self):
        user = add_user('diego', 'diegohuarcaya@upeu.edu.pe')
>>>>>>> 56ca3da6228634e582d203ac043c663a48e90ac1
        with self.client:
            response = self.client.get(f'/users/{user.id}')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertIn('diego', data['data']['username'])
            self.assertIn('diegohuarcaya@upeu.edu.pe', data['data']['email'])
            self.assertIn('success', data['status'])

<<<<<<< HEAD
    def test_single_teacher_no_id(self):
=======
    def test_single_user_no_id(self):
>>>>>>> 56ca3da6228634e582d203ac043c663a48e90ac1
        with self.client:
            response = self.client.get('/users/blah')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 404)
            self.assertIn('El usuario no existe', data['message'])
            self.assertIn('Fail', data['status'])

<<<<<<< HEAD
    def test_single_teacher_incorrect_id(self):
=======
    def test_single_user_incorrect_id(self):
>>>>>>> 56ca3da6228634e582d203ac043c663a48e90ac1
        with self.client:
            response = self.client.get('/users/999')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 404)
            self.assertIn('El usuario no existe', data['message'])
            self.assertIn('Fail', data['status'])

<<<<<<< HEAD
    def test_all_teachers(self):
        add_user('luis', 'luis@upeu.edu.pe', 'greaterthaneight')
        add_user('daniel', 'daniel@gmail.com', 'greaterthaneight')
=======
    def test_all_users(self):
        add_user('luis', 'luis@upeu.edu.pe')
        add_user('daniel', 'daniel@gmail.com')
>>>>>>> 56ca3da6228634e582d203ac043c663a48e90ac1
        with self.client:
            response = self.client.get('/users')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(data['data']['users']), 2)
            self.assertIn('luis', data['data']['users'][0]['username'])
            self.assertIn(
                'luis@upeu.edu.pe', data['data']['users'][0]['email'])
            self.assertIn('daniel', data['data']['users'][1]['username'])
            self.assertIn(
                'daniel@gmail.com', data['data']['users'][1]['email'])

<<<<<<< HEAD
    def test_main_no_teachers(self):
=======
    def test_main_no_users(self):
        """Asegurando que la ruta principal funcione correctamente"""
>>>>>>> 56ca3da6228634e582d203ac043c663a48e90ac1
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Todos los usuarios', response.data)
        self.assertIn(b'<p>No hay usuarios!</p>', response.data)

<<<<<<< HEAD
    def test_main_with_teachers(self):
        add_user('mali', 'mali@upeu.edu.pe', 'greaterthaneight')
        add_user('david', 'david@gmail.com', 'greaterthaneight')
=======
    def test_main_with_users(self):
        """Asegurando que la ruta principal funcione cuando un usuario BD"""
        add_user('mali', 'mali@upeu.edu.pe')
        add_user('david', 'david@gmail.com')
>>>>>>> 56ca3da6228634e582d203ac043c663a48e90ac1
        with self.client:
            response = self.client.get('/')
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Todos los usuarios', response.data)
            self.assertNotIn(b'<p>No hay usuarios!</p>', response.data)
            self.assertIn(b'mali', response.data)
            self.assertIn(b'david', response.data)

<<<<<<< HEAD
    def test_main_add_teachers(self):
=======
    def test_main_add_users(self):
>>>>>>> 56ca3da6228634e582d203ac043c663a48e90ac1
        """Add new users"""
        with self.client:
            response = self.client.post(
                '/',
<<<<<<< HEAD
                data=dict(username='mali', email='mali@upeu.edu.pe', password='greatherthaneight'),
=======
                data=dict(username='mali', email='mali@upeu.edu.pe'),
>>>>>>> 56ca3da6228634e582d203ac043c663a48e90ac1
                follow_redirects=True
            )
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Todos los usuarios', response.data)
            self.assertNotIn(b'<p>No hay usuarios!</p>', response.data)
            self.assertIn(b'mali', response.data)


if __name__ == '__main__':
    unittest.main()
