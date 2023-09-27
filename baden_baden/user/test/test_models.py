from django.test import TestCase
from .. models import CustomUser


class CustomUserModelsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        CustomUser.objects.create_user(
            email='lindTa@gth.com',
            phone_number='79638224555',
            password='Toyota7812'
        )
        CustomUser.objects.create_user(
            phone_number='+79638224556',
            password='France1974',
        )
        CustomUser.objects.create_user(
            email='linda@gth.com',
            password='Binance123'
        )

    def test_email_fields(self):
        user1 = CustomUser.objects.get(pk=1)
        user2 = CustomUser.objects.get(pk=2)
        user3 = CustomUser.objects.get(pk=3)
        self.assertEquals(user1.email, 'lindTa@gth.com')
        self.assertEquals(user2.email, None)
        self.assertEquals(user3.email, 'linda@gth.com')


    def test_phone_number_fields(self):
        user1 = CustomUser.objects.get(pk=1)
        user2 = CustomUser.objects.get(pk=2)
        user3 = CustomUser.objects.get(pk=3)
        self.assertEquals(user1.phone_number, '+7 (963) 822-45-55')
        self.assertEquals(user2.phone_number, '+7 (963) 822-45-56')
        self.assertEquals(user3.phone_number, None)







