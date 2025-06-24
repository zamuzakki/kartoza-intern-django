import factory
from django.contrib.gis.geos import MultiPolygon, Polygon
from factory.django import DjangoModelFactory
from myapp.models import State, Staff, Lake


class StateFactory(DjangoModelFactory):
    class Meta:
        model = State

    name = factory.Sequence(lambda n: f"State {n}")
    population = factory.Faker('random_int', min=100000, max=10000000)
    geom = factory.LazyFunction(
        lambda: MultiPolygon(
            Polygon.from_bbox((-180, -90, 180, 90))
        )
    )


class StaffFactory(DjangoModelFactory):
    class Meta:
        model = Staff

    name = factory.Faker('name')
    age = factory.Faker('random_int', min=18, max=65)
    address = factory.Faker('address')
    salary = factory.Faker('pyfloat', left_digits=5, right_digits=2, positive=True)
    sex = factory.Faker('random_element', elements=['M', 'F'])
    state = factory.SubFactory(StateFactory)


class LakeFactory(DjangoModelFactory):
    class Meta:
        model = Lake

    name = factory.Faker('word')
    geom = factory.LazyFunction(
        lambda: MultiPolygon(
            Polygon.from_bbox((-180, -90, 180, 90))
        )
    )
