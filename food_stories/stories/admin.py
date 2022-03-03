from django.contrib import admin

from stories.models import Contact, Category


admin.site.register([Contact, Category])