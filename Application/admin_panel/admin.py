from django.contrib import admin
from .models import AndroidApp
from .forms import AndroidAppForm

class AndroidAppAdmin(admin.ModelAdmin):
    form = AndroidAppForm  # Optional: Use the custom form
    list_display = ('name', 'points')  # Optional: Display additional fields in the list view

admin.site.register(AndroidApp, AndroidAppAdmin)
