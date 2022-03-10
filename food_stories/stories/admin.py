from django.contrib import admin

from stories.models import Contact, Category, Story, Tag


admin.site.register([Contact, Category, Story, Tag])