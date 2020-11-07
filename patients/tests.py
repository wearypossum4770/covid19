from django.test import TestCase
from django.contrib.auth.models import User
from patients.models.patient import Patient
from django.conf import settings

userModel = settings.AUTH_USER_MODEL


class TestPatients(TestCase):
    @classmethod
    def setUpTestData(cls):
        print(
            "setUpTestData: Run once to set up non-modified data for all class methods."
        )
        User.objects.create(
            first_name="test",
            last_name="test",
            username="test.test",
            email="test.test@example.com",
            password="password123!@#",
        )
        representative = User.objects.get(first_name="test")
        Patient.objects.create(
            edited_by=representative,
            first_name="John",
            middle_name="Daniel",
            last_name="Doe",
            email="John.D.Doe@example.com",
            birth_month=7,
            honorific_suffix="jr",
            birth_day=4,
            birth_year=2003,
            ethinicty=Patient.Ethnicity.MIDDLE_EASTERN,
            consent="",
            gender=Patient.Gender.MALE,
            staff_notes="<p>[automated] looking for test to fail age verification</p><br/>",
        )
        Patient.objects.create(
            edited_by=representative,
            first_name="Jane",
            middle_name="Diane",
            last_name="Doe",
            email="Jane.D.Doe@example.com",
            birth_month=7,
            birth_day=4,
            birth_year=2000,
            ethinicty=Patient.Ethnicity.MIDDLE_EASTERN,
            consent="",
            gender=Patient.Gender.NON_BINARY,
            staff_notes="<p>[automated] Looking for test to pass age verification</p><br/>",
        )

    def test_minor_child(self):
        patient = Patient.objects.get(pk=1)
        assert patient.is_minor_child == True

    def test_non_minor_child(self):
        patient = Patient.objects.get(pk=2)

        assert patient.is_minor_child == True
