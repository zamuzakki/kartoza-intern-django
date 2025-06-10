from django.db import models
from django.contrib.gis.db import models as gis_model

SEX = (
    ('F', 'Female'),
    ('M', 'Male'),
)

class State(models.Model):
    name = models.CharField(max_length=100, unique=True)
    population = models.PositiveIntegerField(null=True, blank=True)
    geom = gis_model.MultiPolygonField(blank=True, null=True)

    def __str__(self):
        return self.name


class Staff(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    age = models.PositiveIntegerField()
    address = models.TextField(blank=True, null=True)
    salary = models.FloatField(blank=True, null=True)
    sex = models.CharField(
        max_length=1,
        blank=True,
        null=True,
        choices=SEX
    )
    state = models.ForeignKey(State, models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Staffs'

    @classmethod
    def do_something(cls):
        print('hello')

    def __str__(self):
        return self.name


class Lake(models.Model):
    name = models.CharField(blank=True, null=True)
    geom = gis_model.MultiPolygonField(blank=True, null=True)

    def __str__(self):
        return self.name