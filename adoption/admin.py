from django.contrib import admin


from .models import Pet
from .models import Vaccine

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display= ["name","submitter","spieces","breed","description","sex","age","submission_date"]

@admin.register(Vaccine)
class VaccineAdmin(admin.ModelAdmin):
    pass
