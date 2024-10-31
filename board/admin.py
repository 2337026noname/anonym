from django.contrib import admin

# Register your models here.

class MemberAdmin(admin.ModelAdmin):
    search_fields = ['name']
