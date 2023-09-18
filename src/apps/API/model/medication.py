from django.core.validators import RegexValidator
from django.db import models

validate_name = RegexValidator(
    regex=r'^[a-zA-Z0-9\-_]*$',
    message='Allowed only letters, numbers, ‘-‘, ‘_’'
)

validate_code = RegexValidator(
    regex=r'^[A-Z0-9\-_]*$',
    message='Allowed only upper case letters, underscore and numbers'
)


class Medication(models.Model):
    name = models.CharField(max_length=100, validators=[validate_name])
    weight = models.PositiveSmallIntegerField()
    code = models.CharField(max_length=100, validators=[validate_code])
    image = models.ImageField()

    def __str__(self):
        return self.name
