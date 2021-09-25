from faker import Faker

from common.constants import Constants

fake = Faker("Ru-ru")


class BasicData:
    def __init__(self, city=None):
        self.city = city

    @classmethod
    def random(cls):
        city = fake.city_name()
        return cls(city)


class NewCourse:
    def __init__(self, full_name=None, short_name=None):
        self.full_name = full_name
        self.short_name = short_name

    @classmethod
    def random(cls):
        full_name = fake.text(max_nb_chars=40)
        short_name = fake.text(max_nb_chars=20) + Constants.TEST_UUID
        return cls(full_name, short_name)
