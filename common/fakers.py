from faker import Faker

fake = Faker("Ru-ru")


class BasicData:
    def __init__(self, city=None):
        self.city = city

    @staticmethod
    def random():
        city = fake.city_name()
        return BasicData(city)


class NewCourse:
    def __init__(self, full_name=None, short_name=None):
        self.full_name = full_name
        self.short_name = short_name

    @staticmethod
    def random():
        full_name = fake.text(max_nb_chars=40)
        short_name = fake.text(max_nb_chars=20)
        return NewCourse(full_name, short_name)
