from django.test import TestCase
from ..managers import CustomUserManager


class ManagersTestCase(TestCase):
    def test_normalise_number(self):
        number = CustomUserManager.phone_normalise('+7!57)(rtejd756903y64')
        number1 = CustomUserManager.phone_normalise('+79028123456')
        self.assertEquals(number, '+7 (577) 569-03-64')
        self.assertEquals(number1, '+7 (902) 812-34-56')
