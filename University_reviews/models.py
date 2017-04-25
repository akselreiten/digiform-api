from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class UniversityReview(models.Model):

    user = models.ForeignKey(User,
                             verbose_name="user",
                             on_delete=models.CASCADE)

    lectures_rating = models.PositiveIntegerField(validators=[MaxValueValidator(5),MinValueValidator(1)],
                                           verbose_name="lectures_rating",)

    assignments_rating = models.PositiveIntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)],
                                                 verbose_name="assignments_rating",)

    difficulty_rating = models.PositiveIntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)],
                                                     verbose_name="difficulty_rating",)

    social_rating = models.PositiveIntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)],
                                                     verbose_name="social_rating",)

    course_availability_rating = models.PositiveIntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)],
                                                verbose_name="course_availability_rating",)

    price_rating = models.PositiveIntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)],
                                                             verbose_name="price_rating",)


    university = models.ForeignKey('universities.University', related_name="university",
                                          verbose_name="university",
                                          on_delete=models.CASCADE)

    description = models.TextField(
        _('description')
    )

