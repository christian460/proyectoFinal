from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Profile
# Register your models here.

User = get_user_model()

class UserAdmin(admin.ModelAdmin):
    search_fields = ['Email']
    class Meta:
        model = User

admin.site.register(User, UserAdmin)
admin.site.register(Profile)
