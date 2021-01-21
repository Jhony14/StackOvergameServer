from django.contrib.auth import get_user_model
from django.test import TestCase


class UsersManagersTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            Correo='normal@user.com', password='foo')
        self.assertEqual(user.Correo, 'normal@user.com')
        self.assertTrue(user.IsActive)
        self.assertFalse(user.IsStaff)
        self.assertFalse(user.is_superuser)
        try:
            self.assertIsNone(user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(Correo='')
        with self.assertRaises(ValueError):
            User.objects.create_user(Correo='', password="foo")

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser('super@user.com', 'foo')
        self.assertEqual(admin_user.Correo, 'super@user.com')
        self.assertTrue(admin_user.IsActive)
        self.assertTrue(admin_user.IsStaff)
        self.assertTrue(admin_user.is_superuser)
        try:
            self.assertIsNone(admin_user.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                Correo='super@user.com', password='foo', is_superuser=False)
