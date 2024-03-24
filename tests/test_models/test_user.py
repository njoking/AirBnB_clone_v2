#!/usr/bin/python3
"""
module to test the User class
"""
import unittest
import os
from models.user import User


class TestUser(unittest.TestCase):
    """
    tests class
    """

    def setUp(self):
        """setup"""
        if not os.path.exists("file.json"):
            os.mknod("file.json")
        self.user = User()

    def tearDown(self):
        """tear down"""
        if os.path.exists("file.json"):
            os.remove("file.json")
        del self.user

    def test_creation(self):
        '''
        ensure correct creation
        '''
        self.assertEqual(self.user.email, '')
        self.assertEqual(self.user.password, '')
        self.assertEqual(self.user.first_name, '')
        self.assertEqual(self.user.last_name, '')

    def test_creation_with_args(self):
        '''
        ensure correct creation with args
        '''
        data = {'id': 3,
                'first_name': 'Betty',
                'last_name': 'Holberton',
                'password': '123',
                'email': 'correo@correo',
                }

        self.user = User(**data)
        self.assertEqual(self.user.id, 3)
        self.assertEqual(self.user.first_name, 'Betty')
        self.assertEqual(self.user.last_name, 'Holberton')
        self.assertEqual(self.user.password, '123')
        self.assertEqual(self.user.email, 'correo@correo')

    def test_types(self):
        '''
        Test types
        '''
        self.assertEqual(type(self.user.email), str)
        self.assertEqual(type(self.user.password), str)
        self.assertEqual(type(self.user.first_name), str)
        self.assertEqual(type(self.user.last_name), str)

    def test_invalid_attributes(self):
        '''
        Test invalid attributes
        '''
        self.user = User({'name': 'Betty', 'my_number': 89})
        self.assertEqual(hasattr(self.user, 'name'), False)
        self.assertEqual(hasattr(self.user, 'my_number'), False)
