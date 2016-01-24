from django.contrib import admin

from .models import (
    Course,
    Category,
    Career,
    Skill,
    SyllabusTopic,
    Instructor,
)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):

    list_display = ('get_badge', 'name', 'category')
    list_display_links = ('get_badge', 'name', 'category')

    list_filter = ('category', 'careers')
    search_fields = (
        'name',
        'slug',
        'category__name',
    )

    prepopulated_fields = {'slug': ('name',)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ('get_badge', 'name')
    list_display_links = ('get_badge', 'name')
    search_fields = ('name',)


@admin.register(Career)
class CareerAdmin(admin.ModelAdmin):

    list_display = ('get_badge', 'name')
    list_display_links = ('get_badge', 'name')
    search_fields = ('name',)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):

    list_display = ('get_image', 'course', 'title')
    list_display_links = ('get_image', 'course', 'title')
    search_fields = ('title', 'coures__name')

    list_filter = ('course',)


@admin.register(SyllabusTopic)
class SyllabusTopicAdmin(admin.ModelAdmin):

    list_display = ('course', 'description')
    list_display_links = ('course', 'description')
    search_fields = ('coures__name', 'description')

    list_filter = ('course',)


@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):

    list_display = (
        'get_picture',
        'name',
        'twitter_handle',
        'job_title',
        'company'
    )
    list_display_links = list_display
    search_fields = ('name', 'job_title', 'company', 'twitter_handle')
    list_filter = ('company',)
