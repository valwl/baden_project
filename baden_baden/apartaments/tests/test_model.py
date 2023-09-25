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



class ReviewImageTestCase(TestCase):
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
        Review.objects.create(
            apartment=apartment,
            rating=5,
            comment='отзыв про апартамент'

        )
        image = SimpleUploadedFile('test_image.jpg', content=b'', content_type='image/jpeg')
        ReviewImage.objects.create(
            apartment=apartment,
            img=image,
        )

    def img_upload_test(self):
        img = ReviewImage.objects.get(pk=1)
        img_url = 'apartments/img/reviews'
        upload = img._meta.get_field('img').upload_to
        self.assertEquals(upload, img_url)



class ApartmentTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        Apartment.objects.create(
            title='Тестовая квартира2',
            apartments_type='Тестовый тип2',
            address='Тестовый адрес2',
            description='Тестовое описание2',
            guests=2,
            max_guests=4,
        )

    def title_apartment_test(self):
        apartment = Apartment.objects.get(pk=1)
        len_title = apartment._meta.get_field('title').max_length
        self.assertEquals(len_title, 100)

