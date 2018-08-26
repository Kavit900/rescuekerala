from django.test import TestCase
# Create your tests here.
from mainapp.models import Request, Volunteer, NGO, Contributor, DistrictManager, DistrictNeed, DistrictCollection, RescueCamp, Person

class RequestTests(TestCase):

	def create_request_object(self):
		return Request.objects.create(
			district="pkd",
			requestee="Kavit",
			requestee_phone="1234567894",
			location="Ernakulam",
			latlng="",
			latlng_accuracy="",
			needwater=False,
			needfood=False,
			needcloth=False,
			needmed=False,
			needtoilet=False,
			needkit_util=False,
			needrescue=False)

	def test_request_district_name(self):
		request = self.create_request_object()
		expected_district_name = f'{request.district}'
		self.assertEqual(expected_district_name, "pkd")	

	def test_request_requestee_name(self):
		request = self.create_request_object()
		expected_requestee_name = f'{request.requestee}'
		self.assertEqual(expected_requestee_name, "Kavit")

	def test_request_requestee_phone(self):
		request = self.create_request_object()
		expected_requestee_phone = f'{request.requestee_phone}'
		self.assertEqual(expected_requestee_phone, "1234567894")

	def test_request_location(self):
		request = self.create_request_object()
		expected_request_location = f'{request.location}'
		self.assertEqual(expected_request_location, "Ernakulam")

class Volunteer(TestCase):

	def create_volunteer_object(self):
		return Volunteer.objects.create(
			name="Kavit",
			district="pkd",
			phone="1234567894",
			organisation="msc",
			area="pkd",
			address="near railway crossing")

class ModelTest(TestCase):

	def test_request_string_representation(self):
		request = Request(
			district="pkd",
			requestee="Kavit",
			requestee_phone= "1234567894",
			location= "Ernakulam",
			latlng= "",
			latlng_accuracy="")
		self.assertEqual(str(request), request.get_district_display()+' '+request.location)

	def test_volunteer_string_representation(self):
		volunteer = Volunteer(
			name="Kavit",
			district="pkd",
			phone="1234567894",
			organisation="msc",
			area="pkd",
			address="near railway crossing")
		self.assertEqual(str(volunteer), volunteer.name)
		
	def test_NGO_string_representation(self):
		ngo = NGO(
			district="pkd",
			organisation="msc",
			organisation_address="1222 CC",
			name="Save Lives")
		self.assertEqual(str(ngo), ngo.name)
		
	def test_contributor_string_representation(self):
		contributor = Contributor(
			district="pkd",
			name="Kavit",
			phone="1234567894",
			address="near railway crossing")
		self.assertEqual(str(contributor), contributor.name+' '+contributor.get_district_display())

	def test_district_manager_string_representation(self):
		districtManager = DistrictManager(
			district="tvm",
			name="Apoorv",
			phone="123456789",
			email="apoorv123@gmail.com")
		self.assertEqual(str(districtManager), districtManager.name+' '+districtManager.get_district_display())

	def test_district_need_string_representation(self):
		districtNeed = DistrictNeed(
			district="tvm",
			needs="Clothes, Water",
			cnandpts="HDFC bank")
		self.assertEqual(str(districtNeed), districtNeed.get_district_display())

	def test_district_collection_string_representation(self):
		districtCollection = DistrictCollection(
			district="pkd",
			collection="Clothes, Utensils")
		self.assertEqual(str(districtCollection), districtCollection.get_district_display())

	def test_rescue_camp_string_representation(self):
		rescueCamp = RescueCamp(
			name="Kerala Flood Relief camp",
			location="Kottayam",
			district="ktm",
			contacts="Phone numbers: 123456789")
		self.assertEqual(str(rescueCamp), rescueCamp.name)

	def test_person_string_representation(self):
		person = Person(
			name="Kavit",
			phone="123456789",
			age="24",
			gender="male",
			address="near railway crossing",
			district="pkd")
		self.assertEqual(str(person), person.name) 