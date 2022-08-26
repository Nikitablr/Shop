from faker import Faker

fake = Faker()


class RegisterData:
    def __init__(self, email: str = None, first_name: str = None, last_name: str = None, password: str = None,
                 password_2: str = None,):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.password_2 = password_2

    @staticmethod
    def random():
        email = fake.email()
        first_name = fake.first_name()
        last_name = fake.last_name()
        password = fake.password()
        password_2 = password
        return RegisterData(email=email, first_name=first_name, last_name=last_name, password=password, \
                                                                                         password_2=password_2)

    @staticmethod
    def random_did_not_match_pass():
        email = fake.email()
        first_name = fake.first_name()
        last_name = fake.last_name()
        password = fake.password()
        password_2 = fake.password()
        return RegisterData(email=email, first_name=first_name, last_name=last_name, password=password, \
                            password_2=password_2)