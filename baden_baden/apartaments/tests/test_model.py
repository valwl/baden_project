from django.test import TestCase
from ..models import Apartment, ApartmentPrice, ApartmentImage, Booking, Review, ReviewImage
from django.core.files.uploadedfile import SimpleUploadedFile


class ApartmentPriceModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        apartment = Apartment.objects.create(
            title='Тестовая квартира',
            apartments_type='Тестовый тип',
            address='Тестовый адрес',
            description='Тестовое описание',
            guests=2,
            max_guests=4,
        )
        ApartmentPrice.objects.create(
          apartment=apartment,
          base_price=10000.00,
          additional_guest_price=2000.00,
        )

    def test_base_prise_max_digits(self):
        price = ApartmentPrice.objects.get(pk=1)
        max_digits = price._meta.get_field('base_price').max_digits
        self.assertEquals(max_digits, 10)



class ApartmentIMageTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        apartment = Apartment.objects.create(
            title='Тестовая квартира',
            apartments_type='Тестовый тип',
            address='Тестовый адрес',
            description='Тестовое описание',
            guests=2,
            max_guests=4,
        )
        image = SimpleUploadedFile('test_image.jpg', content=b'', content_type='image/jpeg')
        ApartmentImage.objects.create(
            apartment=apartment,
            img=image,
        )

    def test_upload_to(self):
        img = ApartmentImage.objects.get(pk=1)
        img_url = 'apartments/img'
        upload = img._meta.get_field('img').upload_to
        self.assertEquals(upload, img_url)

