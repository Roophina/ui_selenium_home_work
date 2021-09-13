from faker import Faker

fake = Faker("Ru-ru")


class BasicData:
    def __init__(self, city=None):
        self.city = city

    @staticmethod
    def random():
        city = fake.city_name()
        return BasicData(city)
