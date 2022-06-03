from datetime import date

from dateutil.relativedelta import relativedelta
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models

from avito.settings import USER_MIN_AGE


def birth_date_check(value: date):
    user_age = relativedelta(date.today(), value).years
    if user_age < USER_MIN_AGE:
        raise ValidationError("Your age is %(value). You have to be at least %(min_age) year old.",
                              params={'value': value,
                                      'min_age': USER_MIN_AGE})


class Location(models.Model):
    name = models.CharField(max_length=50)
    lat = models.DecimalField(max_digits=8, decimal_places=6, null=True)
    lng = models.DecimalField(max_digits=8, decimal_places=6, null=True)

    class Meta:
        verbose_name = "Локация"
        verbose_name_plural = "Локации"

    def __str__(self):
        return self.name


class User(AbstractUser):
    MEMBER = "member"
    MODERATOR = "moderator"
    ADMIN = "admin"
    ROLE = [
        (MEMBER, "Пользователь"),
        (MODERATOR, "Модератор"),
        (ADMIN, "Админ"),
    ]

    role = models.CharField(max_length=9, choices=ROLE, default=MEMBER)
    age = models.PositiveIntegerField(null=True)
    location_id = models.ManyToManyField(Location)

    birth_date = models.DateField(validators=[birth_date_check], null=True)
    email = models.EmailField(unique=True, null=True)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["username"]

    def __str__(self):
        return self.username
