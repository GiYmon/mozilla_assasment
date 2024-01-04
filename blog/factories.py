import factory
from django.conf import settings
from faker import Faker

from .models import Author, Post

fake = Faker()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = settings.AUTH_USER_MODEL
        skip_postgeneration_save = True

    username = factory.LazyFunction(fake.name)
    email = factory.LazyFunction(fake.email)
    password = factory.PostGenerationMethodCall("set_password", "defaultpassword")


class AuthorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Author

    user = factory.SubFactory(UserFactory)
    bio = factory.LazyFunction(fake.text)


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    title = factory.Faker("sentence")
    description = factory.Faker("paragraph")
    author = factory.SubFactory(AuthorFactory)
