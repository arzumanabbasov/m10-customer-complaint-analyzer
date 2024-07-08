import random
from generators.data_loader import DataLoader
from generators.book import Book
from generators.place import Place
from generators.bank import Bank
from generators.music import Music

class Person(DataLoader):
    def __init__(self, ):
        self.male_names = self._load_data('../data/person/male_names.txt')
        self.female_names = self._load_data('..../data/person/female_names.txt')
        self.male_surnames = self._load_data('..../data/person/male_surnames.txt')
        self.female_surnames = self._load_data('..../data/person/female_surnames.txt')
        self.jobs = self._load_data('..../data/person/jobs.txt')
        self.companies = self._load_data('..../data/person/companies.txt')
        self.currencies = self._load_data('..../data/person/currencies.txt')
        self.gender = random.choice(['Kişi', 'Qadın'])
        self.book = Book()
        self.place = Place()
        self.bank = Bank()
        self.music = Music()

    def gender(self):
        return self.gender

    def first_name(self):
        self.gender = random.choice(['Kişi', 'Qadın'])
        return random.choice(self.male_names if self.gender == 'Kişi' else self.female_names)

    def last_name(self):
        return random.choice(self.male_surnames if self.gender == 'Kişi' else self.female_surnames)

    def job(self):
        return random.choice(self.jobs)

    def company(self):
        return random.choice(self.companies)

    def currency(self):
        return random.choice(self.currencies)

    def card_number(self):
        return ''.join(random.choices('0123456789', k=16))

    def email(self):
        domains = ['mail.az', 'gmail.com', 'yahoo.com']
        return f"{self.first_name.lower()}.{self.last_name.lower()}@{random.choice(domains)}"

    def phone_number(self):
        return f"+994 {random.randint(50, 51, 70, 55)} {random.randint(100, 999)}-{random.randint(10, 99)}-{random.randint(10, 99)}"

    def date_of_birth(self):
        year = random.randint(1950, 2000)
        month = random.randint(1, 12)
        day = random.randint(1, 28)  # Simplified to avoid month/day issues
        return f"{year}-{month:02}-{day:02}"

    def age(self):
        return 2024 - int(self.date_of_birth().split('-')[0])

    def social_security_number(self):
        return f"{random.randint(100, 999)}-{random.randint(10, 99)}-{random.randint(1000, 9999)}"

    def driver_license(self):
        return f"{random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}{random.randint(1000000, 9999999)}"

    def passport_number(self):
        return f"{random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}{random.randint(10000000, 99999999)}"

    def height(self):
        return f"{random.randint(150, 200)} cm"

    def weight(self):
        return f"{random.randint(50, 100)} kg"

    def eye_color(self):
        colors = ['Qəhvəyi', 'Mavi', 'Yaşıl', 'Kəhrəba', 'Boz']
        return random.choice(colors)

    def hair_color(self):
        colors = ['Qara', 'Qəhvəyi', 'Sarı', 'Qızıl', 'Boz']
        return random.choice(colors)

    def marital_status(self):
        return random.choice(['Subay', 'Evlənmiş', 'Boşanmış', 'Dul'])

    def education(self):
        degrees = ['Orta Məktəb', 'Kollec', 'Bakalavr', 'Magistr', 'Doktorantura']
        return random.choice(degrees)

    def income(self):
        return f"{random.randint(600, 5000)} AZN"