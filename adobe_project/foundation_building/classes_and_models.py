class IndividualInformation(models.Model):
	individual_id = models.AutoField(primary_key=True)
	first_name = models.Charfield(max_length=25)
	last_name = models.Charfield(max_length=25)
	cell_phone = models.Charfield(max_length=25)
	email = models.EmailField()


class Address(models.Model):
	street = Charfield(max_length=75)
	city = Charfield(max_length=75)
	state = Charfield(max_length=25)
	zip_code = Charfield(max_length=25)


class DriverLicense(models.Model):
	dl_info = models.ForeignKey(IndividualInformation, on_delete=CASCADE)
	dl_num = models.Charfield(max_length=25)
	dl_exp = models.DateField()
	dl_dob = models.DateField()


class CreditCard(models.Model):
	cc_name = models.ForeignKey(IndividualInformation, on_delete=CASCADE)
	cc_num = models.Charfield(max_length=16)
	cc_exp= models.DateField()
	cc_zip = models.Charfield(max_length=25)
	cc_scode = models.Charfield(max_length=6)


class Organization(models.Model)
	org_id = models.AutoField(primary_key=True)
	org_name = models.Charfield(max_length=50)
	org_address = models.ForeignKey(Address, on_delete=models.CASCADE)
	representative = models.ForeignKey(IndividualInformation, on_delete=models.CASCADE)

class SoleCustomer(models.Model):
	cust_info = models.ForeignKey(IndividualInformation, on_delete=models.CASCADE)
	cust_add = models.ForeignKey(Address, on_delete=models.CASCADE)


class OrganizationAffiliate(models.Model):
	aff_info = models.ForeignKey(IndividualInformation, on_delete=models.CASCADE)


class ArrivingFlight(models.Model):
	arriving_airport = models.Charfield(max_length=125)
	arriving_airline = models.Charfield(max_length=125)
	arriving_flight_number = models.Charfield(max_length=25)
	arriving_date = models.DateField()
	arriving_time = models.TimeField()

class DepartingFlight(models.Model):
	departing_airport = models.Charfield(max_length=125)
	departing_airline = models.Charfield(max_length=125)
	departing_flight_number = models.Charfield(max_length=25)
	departing_date = models.DateField()
	departing_time = models.TimeField()