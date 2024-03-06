from django.shortcuts import render
from django.views.generic import TemplateView

from .models import ProjectCategory


class MainPageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['categories'] = ProjectCategory.objects.filter(is_visible=True)

        return context
