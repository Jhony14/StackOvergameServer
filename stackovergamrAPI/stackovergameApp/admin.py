from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import Usuario

# Register your models here.


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = Usuario
    list_display = ('Correo', 'is_staff', 'is_active',)
    list_filter = ('Correo', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('Correo', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('Correo', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('Correo',)
    ordering = ('Correo',)


admin.site.register(Usuario, CustomUserAdmin)
