# admin.py
from django.contrib import admin
from .models import Course, LearningModule, PowerPointPresentation

class LearningModuleInline(admin.StackedInline):
    model = LearningModule

class PowerPointPresentationInline(admin.StackedInline):
    model = PowerPointPresentation

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'instructor', 'main_course')
    list_filter = ('main_course',)
    inlines = [LearningModuleInline, PowerPointPresentationInline]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "main_course":
            kwargs["queryset"] = Course.objects.filter(main_course=None)  # Only show main courses as options
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Course, CourseAdmin)
