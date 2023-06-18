import factory
from faker import Faker
from blog.models import Blog

fake = Faker()

class BlogFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Blog
        
    title = fake.name()
    body = fake.text()
    published = True
 