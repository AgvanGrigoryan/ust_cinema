from django.contrib import admin
from django.utils.safestring import mark_safe

from movies.admin import ReviewAdminInline
from users.models import User


# admin.site.register(User)
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'is_active', 'is_staff', 'image_miniature')
    list_display_links = ('id', 'username')
    readonly_fields = ('image_miniature',)
    search_fields = ('username', 'first_name',)
    search_help_text = 'Поиск по имени, имени пользователя, с учетом регистра.'
    list_editable = ('is_staff',)

    list_filter = ('is_staff',)

    def image_miniature(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="50px" height="auto">')

    image_miniature.short_description = "Предпросмотр изображения"

    inlines = (ReviewAdminInline,)

