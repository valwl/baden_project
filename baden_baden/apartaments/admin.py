from django.contrib import admin

from .models import Apartment, ApartmentImage, ReviewImage, Review, ApartmentPrice, Booking


class AdminInlineApartmentImage(admin.TabularInline):
    model = ApartmentImage
    extra = 1


class AdminInlinePrice(admin.TabularInline):
    model = ApartmentPrice
    extra = 1


class AdminApartment(admin.ModelAdmin):
    fields = ['title', 'apartments_type', 'address', 'description', 'guests', 'max_guests']
    inlines = [AdminInlineApartmentImage, AdminInlinePrice]


class AdminInlineReviewImage(admin.TabularInline):
    model = ReviewImage
    extra = 1


class AdminReview(admin.ModelAdmin):
    fields = ['apartment', 'rating', 'comment']
    inlines = [AdminInlineReviewImage]


admin.site.register(Apartment, AdminApartment)
admin.site.register(Review, AdminReview)
admin.site.register(Booking)
