from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from oauth_pda_app.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    fieldsets = (
        (None, {"fields": ("username", "backend")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "is_staff",
        "is_superuser",
        "backend",
    )
    list_filter = ("is_staff", "is_superuser", "is_active", "groups", "backend")
    search_fields = ("username", "first_name", "last_name", "email")
    readonly_fields = (
        "last_login",
        "date_joined",
        "is_active",
        "username",
        "first_name",
        "last_name",
        "email",
        "backend",
    )
    ordering = ("last_name", "first_name")
    filter_horizontal = (
        "groups",
        "user_permissions",
    )
