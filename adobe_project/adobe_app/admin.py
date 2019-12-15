from django.contrib import admin
from .models import Address, DriverLicense, AdobeVanInfo, CreditCard, AdditionalDriver, ArrivingDepartingFlight, VanRental, IndividualInformation, Organization

# Register your models here.

from import_export import resources
from adobe_app.models import Book

class BookResource(resources.ModelResource):
	class Meta:
		model = Book
		fields = ('id', 'name', 'price',)
		exclude = ('imported', )
		export_order = ('id', 'price', 'author', 'name')

admin.site.register(Book)
admin.site.register(Address)
admin.site.register(DriverLicense)
admin.site.register(CreditCard)
admin.site.register(AdditionalDriver)
admin.site.register(ArrivingDepartingFlight)
admin.site.register(AdobeVanInfo)
admin.site.register(VanRental)
admin.site.register(IndividualInformation)
admin.site.register(Organization)

'''
Address
DriverLicense
CreditCard
AdditionalDriver
ArrivingFlight
DepartingFlight
VanRental
IndividualInformation
Organization
'''