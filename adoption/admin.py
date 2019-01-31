from django.contrib import admin


from .models import Pet
from .models import Vaccine

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    date_hierarchy = 'submission_date'
    list_display= ["name","submitter","spieces","breed","description","sex","age","submission_date"]
    search_fields = ["name","submitter","spieces","breed","description","sex","age","submission_date"]
    list_filter = ['spieces']

@admin.register(Vaccine)
class VaccineAdmin(admin.ModelAdmin):
    pass

admin.site.site_header = "Wisdom Pet Administration"
admin.site.index_title = ""
admin.site.site_title = "Wisdom Pet Administration"