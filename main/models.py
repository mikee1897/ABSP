from django.db import models
from django.db.models import Sum, Avg
from datetime import date, timezone
from decimal import Decimal
# Create your models here.

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

    first_language = models.CharField('first_language', max_length=50, choices=LANGUAGE, null=True, blank=True)
    second_language = models.CharField('second_language', max_length=50, choices=LANGUAGE, null=True, blank=True)
    language_used = models.CharField('language_used', max_length=50, null=True, blank=True, default = "Not Specified")
    quadrant = models.CharField('quadrant', max_length=200, null=True, blank=True)
    name = models.CharField('name', max_length=200, null=True, blank=True)
    idnumber = models.IntegerField('idnumber', null=True, blank=True)
    age = models.IntegerField('age', null=True, blank=True)
    gender = models.CharField('gender', max_length=50, choices=GENDER, null=True, blank=True)
    college = models.CharField('college', max_length=50, choices=COLLEGE, null=True, blank=True)
    email = models.EmailField('email', max_length=50, null=True, blank=True)
    mobile = models.CharField('mobile', max_length=11, null=True, blank=True)
    withdraw_invest = models.CharField('withdraw_invest', max_length=50, null=True, blank=True)
    A_amount =  models.DecimalField('A_amount', max_digits=50, decimal_places=2, null=True, blank=True, default = 0)
    B_amount = models.DecimalField('B_amount', max_digits=50, decimal_places=2, null=True, blank=True, default = 0)
    A_gain_loss = models.DecimalField('A_gain_loss', max_digits=50, decimal_places=2, null=True, blank=True,default = 0)
    B_gain_loss = models.DecimalField('B_gain_loss', max_digits=50, decimal_places=2, null=True, blank=True, default = 0)
    total_coins = models.DecimalField('total_coins', max_digits=50, decimal_places=2, null=True, blank=True, default = 0)
    payout = models.DecimalField('payout', max_digits=50, decimal_places=2, null=True, blank=True, default = 0)

    def save(self, *args, **kwargs):
        self.total_coins =  Decimal(1000) + Decimal(self.A_gain_loss) + Decimal(self.B_gain_loss)
        self.payout = Decimal(self.total_coins) * Decimal(0.05) + Decimal(60)
        super(Participant, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.id)
    