from django.db import models

# Create your models here.

# class CustomerInformation(models.Model):
# 	first_name = models.CharField(max_length=50)
# 	last_name = models.CharField(max_length=50)
# 	email = models.EmailField(max_length=50)
# 	cell_phone = models.CharField(max_length=50)
# 	alt1_phone = models.CharField(max_length=50)
# 	alt2_phone = models.CharField(max_length=50)
# 	address = models.CharField(max_length=50)
# 	city = models.CharField(max_length=50)
# 	state = models.CharField(max_length=50)
# 	country = models.CharField(max_length=50)
# 	zip_code = models.CharField(max_length=5)

# 	def __str__(self):
# 		return self.cell_phone

# class VanRental(models.Model):
# 	renter = models.ForeignKey(CustomerInformation, on_delete=''CASCADE''):
# 	num_of_vans = models.IntegerField
# 	date_of_pickup = models.DateTimeField()#(auto_now=True)
# 	time_of_pickup = models.TimeField(input_value='%H:%M')


# class ShuttleService(models.Model):
# 	pass

# class OrganizationEvent(models.Model):
# 	pass
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField('Book name', max_length=100)
    author = models.ForeignKey(Author, blank=True, null=True, on_delete='CASCADE')
    author_email = models.EmailField('Author email', max_length=75, blank=True)
    imported = models.BooleanField(default=False)
    published = models.DateField('Published', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    categories = models.ManyToManyField(Category, blank=True)

    def __str__(self):
        return self.name

class AdobeVanInfo(models.Model):
	van_id = models.CharField(max_length=25)
	van_year_make_model = models.CharField(max_length=100)
	van_vin = models.CharField(max_length=25)
	van_plate = models.CharField(max_length=25)
	van_size = models.CharField(max_length=25)
	mileage_start = models.CharField(max_length=25, blank=True)
	mileage_end = models.CharField(max_length=25, blank=True)
	van_reg_exp = models.DateField()


class Address(models.Model):
	street = models.CharField(max_length=75, blank=True)
	city = models.CharField(max_length=75, blank=True)
	state = models.CharField(max_length=25, blank=True)
	zip_code = models.CharField(max_length=25, blank=True)

class DriverLicense(models.Model):
	dl_num = models.CharField(max_length=25, blank=True, unique=True)
	dl_exp = models.DateField()#(blank=True)
	dl_dob = models.DateField()#(blank=True)

class CreditCard(models.Model):
	cc_name = models.CharField(max_length=150, blank=True)
	cc_num = models.CharField(max_length=16, unique=True)
	cc_exp= models.DateField()#(blank=True)
	cc_zip = models.CharField(max_length=25)
	cc_scode = models.CharField(max_length=6)

class AdditionalDriver(models.Model):
	full_name = models.CharField(max_length=125, blank=True)
	dl_info = models.ForeignKey(DriverLicense, on_delete='CASCADE', blank=True, null=True)

class ArrivingDepartingFlight(models.Model):


	arriving_airport = models.CharField(max_length=125, blank=True)
	arriving_airline = models.CharField(max_length=125, blank=True)
	arriving_flight_number = models.CharField(max_length=25, blank=True)
	arriving_date_time = models.DateTimeField(blank=True)

# class DepartingFlight(models.Model):
	departing_airport = models.CharField(max_length=125, blank=True)
	departing_airline = models.CharField(max_length=125, blank=True)
	departing_flight_number = models.CharField(max_length=25, blank=True)
	departing_date_time = models.DateTimeField(blank=True)


class IndividualInformation(models.Model):
	individual_id = models.AutoField(primary_key=True, unique=True)
	first_name = models.CharField(max_length=25)
	last_name = models.CharField(max_length=25)
	cell_phone = models.CharField(max_length=25, unique=True)
	email = models.EmailField(unique=True)
	cust_address = models.ForeignKey(Address, on_delete='CASCADE', blank=True, null=True)
	cust_driver_license = models.ForeignKey(DriverLicense, on_delete='CASCADE', blank=True, null=True)

	cust_credit_card = models.ForeignKey(CreditCard, on_delete='CASCADE', blank=True, null=True)
	indi_info = '{}, {} cell: {}'.format(last_name, first_name, email)

	def __str__(self):
		return self.indi_info

class Organization(models.Model):
	org_id = models.AutoField(primary_key=True)
	org_name = models.CharField(max_length=50)
	org_address = models.ForeignKey(Address, on_delete='CASCADE', blank=True,  null=True)
	org_representative = models.ForeignKey(IndividualInformation, on_delete='CASCADE', blank=True, null=True)

	dl_num = models.CharField(max_length=25, blank=True)
	dl_exp = models.DateTimeField(blank=True)
	dl_dob = models.DateTimeField(blank=True)
	cc_num = models.CharField(max_length=16, blank=True)
	cc_exp= models.DateTimeField(blank=True)
	cc_zip = models.CharField(max_length=25, blank=True)

class VanRental(models.Model):
	rentee_name = models.ForeignKey(IndividualInformation, on_delete='CASCADE', blank=True)
	org_name = models.ForeignKey(Organization, on_delete='CASCADE', blank=True)
	rental_date_start = models.DateTimeField(blank=True)
	rental_date_end = models.DateTimeField(blank=True)
	num_of_vans = models.IntegerField(blank=True)
	rate_charge = models.IntegerField(blank=True)
	mileage_over_charge = models.IntegerField(blank=True)
	late_charge = models.IntegerField(blank=True)
	fuel_charge = models.IntegerField(blank=True)
	damage_charge = models.IntegerField(blank=True)
	additional_driver = models.IntegerField(blank=True)
	under_age = models.IntegerField(blank=True)
	drop_fee = models.IntegerField(blank=True)
	mexico_insurance = models.IntegerField(blank=True)
	cleaning_fee = models.IntegerField(blank=True)
	other_charges = models.IntegerField(blank=True)
	surcharge = models.IntegerField(blank=True)
	license_tax = models.IntegerField(blank=True)
	sales_tax = models.IntegerField(blank=True)
	airport_access_fee = models.IntegerField(blank=True)
	subtotal_out = models.IntegerField(blank=True)
	total_due = models.IntegerField(blank=True)
	subtotal_in = models.IntegerField(blank=True)
	grand_total = models.IntegerField(blank=True)
