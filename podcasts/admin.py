from django.contrib import admin

# Register your models here.

from .models import Episode 

@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
     list_disply = ('podcat_name', "title","pub_date")

     