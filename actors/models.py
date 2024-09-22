from django.db import models


NATIONALITY_CHOICES = (
    ('USA', 'Estados Unidos'),
    ('UK', 'Reino Unido'),
    ('Canada', 'Canadá'),
    ('Australia', 'Australia'),
    ('France', 'Francia'),
    ('Germany', 'Alemania'),
    ('Spain', 'España'),
    ('Japan', 'Japon'),
    ('China', 'China'),
    ('India', 'India'),
    ('Brazil', 'Brasil'),
    ('Russia', 'Rusia'),
)


class Actor(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField(null=True, blank=True)
    nationality = models.CharField(
        max_length=100,
        choices=NATIONALITY_CHOICES,
        blank=True,
        null=True,
        default='Brazil'
    )
    def __str__(self):
        return self.name
    