from django.contrib import admin
from HomeApp.models import Experience, Education, Award

# Register your models here.


class AdminExperience(admin.ModelAdmin):
    list_display = ['title', 'company', 'dateStart', 'dateEnd']  # COL DATA
    search_fields = ['title', 'company']  # SEARCH DATA


class AdminEducation(admin.ModelAdmin):
    list_display = ['title', 'school', 'dateStart', 'dateEnd']  # COL DATA
    search_fields = ['title', 'school']  # SEARCH DATA


class AdminAward(admin.ModelAdmin):
    list_display = ['title']  # COL DATA
    search_fields = ['title']  # SEARCH DATA


admin.site.register(Experience, AdminExperience)
admin.site.register(Education, AdminEducation)
admin.site.register(Award, AdminAward)
