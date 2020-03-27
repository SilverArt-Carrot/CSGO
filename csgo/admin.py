from django.contrib import admin
from .models import CSgoUser, Gun


# Register your models here.

class CSgoUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password',)


class GunAdmin(admin.ModelAdmin):
    fieldsets = [
        ('枪名', {'fields': ['name']}),
        ('类别', {'fields': ['cate']}),
    ]
    list_display = ('name', 'cate',)
    list_filter = ['cate']
    search_fields = ['gun']


admin.site.register(CSgoUser, CSgoUserAdmin)
admin.site.register(Gun, GunAdmin)