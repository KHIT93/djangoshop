from django.contrib import admin
from .models.app_setting import AppSetting
# Register your models here.

class AppSettingModelAdmin(admin.ModelAdmin):
    list_display = ['key', 'value']
    class Meta:
        model = AppSetting

admin.site.register(AppSetting, AppSettingModelAdmin)
