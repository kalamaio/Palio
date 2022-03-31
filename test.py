from faker import Faker
from faker.providers import lorem

fake = Faker ('it_IT')
fake.add_provider (lorem)




print (fake.paragraph (nb_sentences = 30))