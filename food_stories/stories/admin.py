from django.contrib import admin

from stories.models import Contact, Category, Story, Tag

class StoryInlineAdmin(admin.TabularInline):
    model = Story


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [StoryInlineAdmin, ]


@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author', 'created_at')
    list_filter = ('category__title', 'created_at', )
    search_fields = ('title', 'author__username')
    fieldsets = [
        ('Standard info', {
            'fields': ('title', 'category', 'author', ),
            'classes': ('wide',)
        }),
        ('Other', {
            'fields': ('tags', )
        }),
    ]



admin.site.register([Contact, Tag])