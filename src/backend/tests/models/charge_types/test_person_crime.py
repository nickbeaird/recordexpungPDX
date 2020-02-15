import unittest

from datetime import datetime, timedelta

from expungeservice.models.expungement_result import EligibilityStatus
from expungeservice.models.charge_types.person_crime import PersonCrime

from tests.factories.charge_factory import ChargeFactory
from expungeservice.models.disposition import Disposition


class TestSingleChargeConvictionsPersonCrime(unittest.TestCase):
    def setUp(self):
        last_week = datetime.today() - timedelta(days=7)
        self.single_charge = ChargeFactory.build(disposition=Disposition(ruling="Convicted", date=last_week))
        self.charges = []

    def create_recent_charge(self):
        charge = ChargeFactory.save(self.single_charge)
        return charge

    def test_misdemeanor_sex_crime(self):
        self.single_charge["name"] = "Sexual Abuse in the Third Degree"
        self.single_charge["statute"] = "163.415"
        self.single_charge["level"] = "Misdemeanor Class A"
        misdemeanor_class_a_convicted = self.create_recent_charge()
        self.charges.append(misdemeanor_class_a_convicted)

        assert isinstance(misdemeanor_class_a_convicted, PersonCrime)
        assert misdemeanor_class_a_convicted.type_name == "Person Crime"
        assert misdemeanor_class_a_convicted.expungement_result.type_eligibility.status is EligibilityStatus.INELIGIBLE
        assert misdemeanor_class_a_convicted.expungement_result.type_eligibility.reason == "Ineligible under 137.225(5)"

    def test_min_statute_range_for_crimes_against_persons(self):
        self.single_charge["statute"] = "163.305"
        convicted_charge = self.create_recent_charge()
        self.charges.append(convicted_charge)

        assert isinstance(convicted_charge, PersonCrime)
        assert convicted_charge.type_name == "Person Crime"
        assert convicted_charge.expungement_result.type_eligibility.status is EligibilityStatus.INELIGIBLE
        assert convicted_charge.expungement_result.type_eligibility.reason == "Ineligible under 137.225(5)"

    def test_max_statute_range_for_crimes_against_persons(self):
        self.single_charge["statute"] = "163.479"
        convicted_charge = self.create_recent_charge()
        self.charges.append(convicted_charge)

        assert isinstance(convicted_charge, PersonCrime)
        assert convicted_charge.type_name == "Person Crime"
        assert convicted_charge.expungement_result.type_eligibility.status is EligibilityStatus.INELIGIBLE
        assert convicted_charge.expungement_result.type_eligibility.reason == "Ineligible under 137.225(5)"

    def test_min_statute_range_for_other_crimes_against_persons(self):
        self.single_charge["statute"] = "163.670"
        convicted_charge = self.create_recent_charge()
        self.charges.append(convicted_charge)

        assert isinstance(convicted_charge, PersonCrime)
        assert convicted_charge.type_name == "Person Crime"
        assert convicted_charge.expungement_result.type_eligibility.status is EligibilityStatus.INELIGIBLE
        assert convicted_charge.expungement_result.type_eligibility.reason == "Ineligible under 137.225(5)"

    def test_max_statute_range_for_other_crimes_against_persons(self):
        self.single_charge["statute"] = "163.693"
        convicted_charge = self.create_recent_charge()
        self.charges.append(convicted_charge)

        assert isinstance(convicted_charge, PersonCrime)
        assert convicted_charge.type_name == "Person Crime"
        assert convicted_charge.expungement_result.type_eligibility.status is EligibilityStatus.INELIGIBLE
        assert convicted_charge.expungement_result.type_eligibility.reason == "Ineligible under 137.225(5)"

    def test_min_statute_range_for_promoting_prostitution(self):
        self.single_charge["statute"] = "167.008"
        convicted_charge = self.create_recent_charge()
        self.charges.append(convicted_charge)

        assert isinstance(convicted_charge, PersonCrime)
        assert convicted_charge.type_name == "Person Crime"
        assert convicted_charge.expungement_result.type_eligibility.status is EligibilityStatus.INELIGIBLE
        assert convicted_charge.expungement_result.type_eligibility.reason == "Ineligible under 137.225(5)"

    def test_max_statute_range_for_promoting_prostitution(self):
        self.single_charge["statute"] = "167.107"
        convicted_charge = self.create_recent_charge()
        self.charges.append(convicted_charge)

        assert isinstance(convicted_charge, PersonCrime)
        assert convicted_charge.type_name == "Person Crime"
        assert convicted_charge.expungement_result.type_eligibility.status is EligibilityStatus.INELIGIBLE
        assert convicted_charge.expungement_result.type_eligibility.reason == "Ineligible under 137.225(5)"

    def test_min_statute_range_for_obscenity_and_minors(self):
        self.single_charge["statute"] = "167.057"
        convicted_charge = self.create_recent_charge()
        self.charges.append(convicted_charge)

        assert isinstance(convicted_charge, PersonCrime)
        assert convicted_charge.type_name == "Person Crime"
        assert convicted_charge.expungement_result.type_eligibility.status is EligibilityStatus.INELIGIBLE
        assert convicted_charge.expungement_result.type_eligibility.reason == "Ineligible under 137.225(5)"

    def test_max_statute_range_for_obscenity_and_minors(self):
        self.single_charge["statute"] = "167.080"
        convicted_charge = self.create_recent_charge()
        self.charges.append(convicted_charge)

        assert isinstance(convicted_charge, PersonCrime)
        assert convicted_charge.type_name == "Person Crime"
        assert convicted_charge.expungement_result.type_eligibility.status is EligibilityStatus.INELIGIBLE
        assert convicted_charge.expungement_result.type_eligibility.reason == "Ineligible under 137.225(5)"

    def test_rape_class_c_felony(self):
        self.single_charge["name"] = "Rape in the Third Degree"
        self.single_charge["statute"] = "163.355"
        self.single_charge["level"] = "Felony Class C"
        sex_crime_charge = self.create_recent_charge()
        self.charges.append(sex_crime_charge)

        assert isinstance(sex_crime_charge, PersonCrime)
        assert sex_crime_charge.type_name == "Person Crime"
        assert sex_crime_charge.expungement_result.type_eligibility.status is EligibilityStatus.INELIGIBLE