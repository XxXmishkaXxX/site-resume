from django.test import TestCase
from django.utils import timezone
from .models import CustomUser


class CustomUserModelTestCase(TestCase):

    def test_create_user(self):
        """
        Тестирование создания пользователя
        """
        user = CustomUser.objects.create_user(
            email='test@example.com',
            full_name='Test User',
            sex='M',
            password='password123'
        )
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.full_name, 'Test User')
        self.assertEqual(user.sex, 'M')
        self.assertTrue(user.date_joined <= timezone.now())
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)

    def test_create_superuser(self):
        """
        Тестирование создания суперпользователя
        """
        admin_user = CustomUser.objects.create_superuser(
            email='admin@example.com',
            full_name='Admin User',
            sex='M',
            password='adminpassword123'
        )
        self.assertEqual(admin_user.email, 'admin@example.com')
        self.assertEqual(admin_user.full_name, 'Admin User')
        self.assertEqual(admin_user.sex, 'M')
        self.assertTrue(admin_user.date_joined <= timezone.now())
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_superuser)
        self.assertTrue(admin_user.is_staff)

    def test_str_method(self):
        """
        Тестирование метода __str__ модели
        """
        user = CustomUser.objects.create_user(
            email='test@example.com',
            full_name='Test User',
            sex='M',
            password='password123'
        )
        self.assertEqual(str(user), 'test@example.com')
