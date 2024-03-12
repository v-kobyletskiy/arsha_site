from django.shortcuts import render
from django.views.generic import TemplateView

from .models import ProjectCategory, Project, Employee, Skill


class MainPageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['categories'] = ProjectCategory.objects.filter(is_visible=True)
        context['projects'] = Project.objects.filter(is_visible=True)
        context['employees'] = Employee.objects.filter(is_visible=True)
        context['skills'] = Skill.objects.filter(is_visible=True)

        return context
