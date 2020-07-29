from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import User, Elder, Younger, YoungerRequest, ElderApproval, Profile, Transactions, Completed

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "username", "is_younger", "is_elder"]


class ElderAdmin(admin.ModelAdmin):
    list_display = ["user", "need_help", "funds"]

class YoungerAdmin(admin.ModelAdmin):
    list_display = ["user"]

class ElderApprovalAdmin(admin.ModelAdmin):
    list_display = ["id", "approved_by", "approved_to", "date_approved"]

class YoungerRequestAdmin(admin.ModelAdmin):
    list_display = ["id", "request_by", "request_to", "date_requested"]

class ProfileAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "display_name", "is_younger_profile", "is_elder_profile"]

class TranscationsAdmin(admin.ModelAdmin):
    list_display = ['id', 'care_seeker', 'care_giver', 'date_approved','end_date']


class CompletedAdmin(admin.ModelAdmin):
    list_display = ['id', 'care_to', 'care_by', 'date_started', 'date_ended']



admin.site.register(User, UserAdmin)
admin.site.register(Elder, ElderAdmin)
admin.site.register(Younger, YoungerAdmin)
admin.site.register(YoungerRequest, YoungerRequestAdmin)
admin.site.register(ElderApproval, ElderApprovalAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Transactions,TranscationsAdmin)
admin.site.register(Completed,CompletedAdmin)
