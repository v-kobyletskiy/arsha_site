from django.contrib import admin
from .models import ProjectCategory


@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('id', 'name', 'slug', 'position', 'is_visible')
    list_editable = ('name', 'position', 'is_visible')
