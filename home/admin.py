from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import ProjectCategory, Project, Employee, Skill, Message, GeneralInfo, FrequentlyQuestion, Service

admin.site.register(GeneralInfo)


@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('id', 'name', 'slug', 'position', 'is_visible')
    list_editable = ('name', 'position', 'is_visible')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('photo_src_tag', 'name', 'slug', 'description', 'position', 'is_visible', 'category')
    list_editable = ('name', 'slug', 'description', 'position', 'is_visible', 'category')
    list_filter = ('category', 'is_visible')
    search_fields = ('name',)

    def photo_src_tag(self, obj):
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}' width=50 height=50>")

    photo_src_tag.short_description = 'Dish photo'


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('photo_src_tag', 'name', 'surname', 'appointment', 'description', 'position', 'is_visible',
                    'twitter_profile', 'facebook_profile', 'instagram_profile', 'linkedin_profile')
    list_editable = ('name', 'surname', 'appointment', 'description', 'position', 'is_visible',
                     'twitter_profile', 'facebook_profile', 'instagram_profile', 'linkedin_profile')

    def photo_src_tag(self, obj):
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}' width=50 height=50>")

    photo_src_tag.short_description = 'Employee photo'


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'progress', 'is_visible', 'position')
    list_editable = ('name', 'progress', 'is_visible', 'position')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'subject', 'email', 'message', 'is_processed', 'created_at')
    list_editable = ('is_processed',)
    list_filter = ('created_at', )


@admin.register(FrequentlyQuestion)
class FrequentlyQuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'answer', 'position', 'is_visible')
    list_editable = ('question', 'answer', 'position', 'is_visible')


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'position', 'is_visible')
    list_editable = ('title', 'description', 'position', 'is_visible')

