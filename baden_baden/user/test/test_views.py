from django.test import TestCase
from .. models import CustomUser
from django.urls import reverse
from .. models import Profile


class RegisterUserTestCase(TestCase):
    def test_register_view(self):
        register_data = {'email': 'linda@grt.com',
                         'phone_number': '893165748934',
                         'first_name': 'vl',
                         'last_name': 'rdg',
                         'password1': 'Binance324',
                         'password2': 'Binance324',
                         }
        response = self.client.post(reverse('register'), data=register_data)
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))
        user = CustomUser.objects.filter(email=register_data['email']).exists()
        print('---------', user)
        user_profile = Profile.objects.filter(user=user).exists()
        self.assertTrue(user)
        self.assertTrue(user_profile)

    def test_register_validated_data(self):
        invalid_data = {#'email': 'linda@grt.com',
                         'phone_number': '8931657489347679-6887',
                         'first_name': 'vl',
                         'last_name': 'rdg',
                         'password1': 'Binance334',
                         'password2': 'Binance324',
                         }
        response = self.client.post(reverse('register'), data=invalid_data)
        self.assertEquals(response.status_code, 200)
        #self.assertFormError(response, 'form', 'password2', 'The two password fields didn’t match.')
        #self.assertFormError(response, 'form', 'phone_number', 'Phone number must be 10 or 11 digits long.')









