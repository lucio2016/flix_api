from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from movies.models import Movie


class Review(models.Model):
    movie = models.ForeignKey(
        Movie,
        on_delete=models.PROTECT,
        related_name='reviews',
    )
    stars = models.IntegerField(
        validators=[
            MinValueValidator(0, 'Não pode ser inferior a 0'),
            MaxValueValidator(5, 'Não pode ser superior a 0')
        ]
    )
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.review
