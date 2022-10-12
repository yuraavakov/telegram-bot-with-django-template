from django.contrib import admin
from adminpanel.forms import ProfileForm
from adminpanel.models import Profile, Message


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'external_id', 'name')
    form = ProfileForm


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile', 'text', 'created_date')
