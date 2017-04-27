from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class UniversityReview(models.Model):

    #user from foreign key
    user = models.ForeignKey(User,
                             verbose_name="user",
                             on_delete=models.CASCADE)

    #lecture rating from 1 to 5
    lectures_rating = models.PositiveIntegerField(validators=[MaxValueValidator(5),MinValueValidator(1)],
                                           verbose_name="lectures_rating",)

    #rating from 1 to 5
    assignments_rating = models.PositiveIntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)],
                                                 verbose_name="assignments_rating",)

    #rating from 1 to 5
    difficulty_rating = models.PositiveIntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)],
                                                     verbose_name="difficulty_rating",)

    #rating from 1 to 5
    social_rating = models.PositiveIntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)],
                                                     verbose_name="social_rating",)

    #rating from 1 to 5
    course_availability_rating = models.PositiveIntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)],
                                                verbose_name="course_availability_rating",)

    #rating from 1 to 5
    price_rating = models.PositiveIntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)],
                                                             verbose_name="price_rating",)

    #university from foreign key
    university = models.ForeignKey('universities.University', related_name="university",
                                          verbose_name="university",
                                          on_delete=models.CASCADE)

    #description of stay
    description = models.TextField(
        _('description')
    )

