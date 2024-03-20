from django.shortcuts import render
from django.views.generic import TemplateView

from .models import ProjectCategory, Project, Employee, Skill
from .forms import MessageForm


class MainPageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        message_form = MessageForm()

        context['categories'] = ProjectCategory.objects.filter(is_visible=True)
        context['projects'] = Project.objects.filter(is_visible=True)
        context['employees'] = Employee.objects.filter(is_visible=True)
        context['skills'] = Skill.objects.filter(is_visible=True)
        context['message_form'] = message_form

        return context

    def post(self, request, *args, **kwargs):
        message_form = MessageForm(request.POST)
        if message_form.is_valid():
            message_form.save()
            message_form = MessageForm()
            return render(request, 'index.html', {'message_form': message_form})
        else:
            return render(request, 'index.html', {'message_form': message_form})
