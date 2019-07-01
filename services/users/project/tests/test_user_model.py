import unittest
from sqlalchemy.exc import IntegrityError
from project import db
from project.api.models import User
from project.tests.base import BaseTestCase
from project.tests.utils import add_user


class TestUserModel(BaseTestCase):

    def test_add_user(self):
<<<<<<< HEAD
        user = add_user('justatest1', 'test@test.com', 'greaterthaneight')
=======
        user = add_user('justatest1', 'test@test.com')
>>>>>>> 56ca3da6228634e582d203ac043c663a48e90ac1
        db.session.add(user, id)
        self.assertEqual(user.username, 'justatest1')
        self.assertEqual(user.email, 'test@test.com')
        self.assertTrue(user.active)

    def test_add_user_duplicate_username(self):
<<<<<<< HEAD
        add_user('justatest1', 'test@test.com', 'greaterthaneight')
=======
        add_user('justatest1', 'test@test.com')
>>>>>>> 56ca3da6228634e582d203ac043c663a48e90ac1
        duplicate_user = User(
            username='justatest1',
            email='test@test2.com',
        )
        db.session.add(duplicate_user)
        self.assertRaises(IntegrityError, db.session.commit)

    def test_add_user_duplicate_email(self):
<<<<<<< HEAD
        add_user('justatest1', 'test@test.com', 'greaterthaneight')
=======
        add_user('justatest1', 'test@test.com')
>>>>>>> 56ca3da6228634e582d203ac043c663a48e90ac1
        duplicate_user = User(
            username='justanothertest1',
            email='test@test.com',
        )
        db.session.add(duplicate_user)
        self.assertRaises(IntegrityError, db.session.commit)

    def test_in_json(self):
<<<<<<< HEAD
        user = add_user('justatest1', 'test@test.com', 'greaterthaneight')
        self.assertTrue(isinstance(user.to_json(), dict))

    def test_passwords_are_random(self):
        user_one = add_user('pachemon', 'pache@mon.com', 'greaterthaneightq')
        user_two = add_user('vaca', 'vaca@test.com', 'greaterthaneight')
        self.assertNotEqual(user_one.password, user_two.password)

=======
        user = add_user('justatest1', 'test@test.com')
        self.assertTrue(isinstance(user.to_json(), dict))

>>>>>>> 56ca3da6228634e582d203ac043c663a48e90ac1

if __name__ == '__main__':
    unittest.main()
