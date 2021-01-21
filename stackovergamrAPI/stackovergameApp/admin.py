from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import Usuario

# Register your models here.


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = Usuario
    list_display = ('Correo', 'IsStaff', 'IsActive',)
    list_filter = ('Correo', 'IsStaff', 'IsActive',)
    fieldsets = (
        (None, {'fields': ('Correo', 'password')}),
        ('Permissions', {'fields': ('IsStaff', 'IsActive')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('Correo', 'password1', 'password2', 'IsStaff', 'IsActive')}
         ),
    )
    search_fields = ('Correo',)
    ordering = ('Correo',)


admin.site.register(Usuario, CustomUserAdmin)
