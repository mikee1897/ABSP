from django.contrib import admin

# Register your models here.
from main.models import Participant, Tally

admin.site.register(Participant)
admin.site.register(Tally)


