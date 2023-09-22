from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(AndroidApp)
# admin.site.register(UserProfile)
admin.site.register(Task)

class UserProfileAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if change:  # Only execute for existing instances (not new ones)
            app = AndroidApp.objects.get(pk=1)  # Replace app_id with the actual app ID
            obj.get_points_earned(app)

# Register the UserProfile model with the custom admin class
admin.site.register(UserProfile, UserProfileAdmin)