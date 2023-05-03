from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Comment, Follow, Group, Post


class PostAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "pub_date",
        "text",
        "author",
        "group",
        "image_preview",
        "image",
    )
    readonly_fields = ("pub_date", "image_preview")
    list_editable = ("group", "image")
    search_fields = ("text",)
    list_filter = ("pub_date", "author")
    empty_value_display = "-пусто-"
    list_per_page = 10
    save_on_top = True
    actions_on_top = True

    def image_preview(self, obj):
        if not obj.image:
            return ""
        return mark_safe(
            f'<img src="{obj.image.url}"  style="max-height: 100px;">'
        )

    image_preview.short_description = "Превью"


class GroupAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "description")


class CommentAdmin(admin.ModelAdmin):
    list_display = ("pk", "text", "created", "author", "post")
    readonly_fields = ("created", "author", "post")
    search_fields = ("text", "author")
    list_filter = ("created", "author")
    empty_value_display = "-пусто-"


admin.site.register(Post, PostAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Follow)

admin.site.site_header = "Административная панель Yatube"
admin.site.index_title = "Настройки Yatube"
admin.site.site_title = "Административная панель Yatube"
