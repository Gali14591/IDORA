from django.test import TestCase
from .serializers import UserRegistrationSerializer

class RegisterSerializerTests(TestCase):
    def test_password_mismatch(self):
        data = {'phone': '+111', 'role': 'citizen', 'password': 'a', 'password2': 'b'}
        s = UserRegistrationSerializer(data=data)
        self.assertFalse(s.is_valid())
        self.assertIn('password', s.errors)

    def test_missing_fields(self):
        s = UserRegistrationSerializer(data={})
        self.assertFalse(s.is_valid())
        self.assertIn('phone', s.errors)
