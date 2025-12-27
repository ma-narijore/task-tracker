from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .models import Worker, Position


@admin.register(Worker)
class WorkerAdmin(UserAdmin):
    model = Worker

    # ✅ Fields shown in admin list
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "position",
        "is_staff",
        "is_active",
    )

    list_filter = ("is_staff", "is_active", "position")

    search_fields = ("username", "email", "first_name", "last_name")

    ordering = ("username",)

    # ❌ Fields that should NOT be editable
    readonly_fields = ("last_login", "date_joined")

    # ✅ Fields shown when editing an existing user
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {
            "fields": ("first_name", "last_name", "email", "position")
        }
         ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

    # ✅ Fields shown when creating a new user
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "email",
                    "first_name",
                    "last_name",
                    "position",
                    "password1",
                    "password2",
                ),
            },
        ),
    )


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)
