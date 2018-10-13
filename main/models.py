from django.db import models
from django.db.models import Sum, Avg
from datetime import date, timezone
from decimal import Decimal
# Create your models here.
import random
import decimal
class Participant(models.Model):
    LANGUAGE = (
        ('English', 'English'),
        ('Tagalog', 'Tagalog'),
        ('Korean', 'Korean'),
        ('Japanese', 'Japanese'),
        ('Mandarin', 'Mandarin'),
        ('Hokkien', 'Hokkien'),
        ('Cebuano', 'Cebuano'),
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

    GENDER = (
        ('M', 'M'),
        ('F', 'F'),
    )

    first_language = models.CharField('first_language', max_length=50, choices=LANGUAGE, null = True)
    second_language = models.CharField('second_language', max_length=50, choices=LANGUAGE, null = True)
    language_used = models.CharField('language_used', max_length=50, null = True)
    quadrant = models.CharField('quadrant', max_length=200, null = True)
    treatment = models.IntegerField('treatment', null = True)
    name = models.CharField('name', max_length=200, null = True)
    idnumber = models.IntegerField('idnumber',null = True)
    age = models.IntegerField('age', null = True)
    gender = models.CharField('gender', max_length=50, choices=GENDER, null = True)
    college = models.CharField('college', max_length=50, choices=COLLEGE, null = True)
    email = models.EmailField('email', max_length=50, null = True)
    mobile = models.CharField('mobile', max_length=11, null = True)
    withdraw_invest = models.IntegerField('withdraw_invest',null = True)
    investment = models.DecimalField('investment', max_digits=50, decimal_places=2, default=1000)
    A_amount =  models.DecimalField('A_amount', max_digits=50, decimal_places=2, null = True)
    B_amount = models.DecimalField('B_amount', max_digits=50, decimal_places=2, null = True)
    A_generated_percent = models.DecimalField('A_generated_percent', max_digits=50, decimal_places=2, default = 0)
    B_generated_percent = models.DecimalField('B_generated_percent', max_digits=50, decimal_places=2, default = 0)
    A_gain_loss = models.DecimalField('A_gain_loss', max_digits=50, decimal_places=2, null = True, default = 0)
    B_gain_loss = models.DecimalField('B_gain_loss', max_digits=50, decimal_places=2, null = True, default = 0)
    ecu = models.DecimalField('ecu', max_digits=50, decimal_places=2, default = 0)
    payout = models.DecimalField('payout', max_digits=50, decimal_places=2, default = 0)

    def save(self, *args, **kwargs):
        self.ecu =  Decimal(self.investment) + Decimal(self.A_gain_loss) + Decimal(self.B_gain_loss)
        self.payout = Decimal(self.ecu) * Decimal(0.07) + Decimal(60)
        super(Participant, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.idnumber) + " - " + str(self.name)
    