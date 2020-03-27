from django.contrib import admin
from .models import Category, Weapon, User


# Register your models here.
class WeaponAdmin(admin.ModelAdmin):
    fieldsets = [
        ('枪名', {'fields': ['gun']}),
        ('类别', {'fields': ['which_cate']}),
    ]
    list_display = ('gun',)
    list_filter = ['which_cate']
    search_fields = ['gun']


class WeaponInline(admin.TabularInline):
    model = Weapon
    extra = 5


class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        ('枪械种类', {'fields': ['cate']}),
    ]
    inlines = [WeaponInline]
    list_display = ('cate',)
    search_fields = ['cate']


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password',)


admin.site.register(Weapon, WeaponAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(User, UserAdmin)
