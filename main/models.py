from django.db import models
from django.db.models import Sum, Avg
from datetime import date, timezone

# Create your models here.

class Participant(models.Model):
    LANGUAGE = (
        ('Filipino', 'Filipino'),
        ('English', 'English'),
        ('Hokkien', 'Hokkien'),
        ('Mandarin', 'Mandarin'),
        ('Korean', 'Korean'),
        ('Japanese', 'Japanese'),
        ('Bisaya/Cebuano', 'Bisaya/Cebuano'),
    )

    COLLEGE = (
        ('BAGCED', 'BAGCED'),
        ('CCS', 'CCS'),
        ('COL', 'COL'),
        ('CLA', 'CLA'),
        ('COS', 'COS'),
        ('GCOE', 'GCOE'),
        ('RVRCOB', 'RVRCOB'),
        ('SOE', 'SOE'),
    )

    idnumber = models.CharField(max_length=8, default='not specified')
    first_name = models.CharField(max_length=200, default='not specified')
    last_name = models.CharField(max_length=200, default='not specified')
    mobile = models.CharField(max_length=11, default='not specified')
    email = models.EmailField(max_length=200, default='not specified')
    birthday = models.DateField(max_length=200, default='not specified')
    college = models.CharField('college', choices=COLLEGE, max_length=200, default='not specified')
    degree = models.CharField(max_length=200, default='not specified')
    language1 = models.CharField('language1', choices=LANGUAGE, max_length=200, default='not specified', null=True, blank=True)
    language2 = models.CharField('language2', choices=LANGUAGE, max_length=200, default='not specified', null=True, blank=True)
    question1 = models.CharField(max_length=200, default='not specified', null=True, blank=True)
    question2 = models.CharField(max_length=200, default='not specified', null=True, blank=True)
    date = models.DateField('date_counted', auto_now_add=True)

    def __str__(self):
        return str(self.last_name) +', ' + str(self.first_name)
