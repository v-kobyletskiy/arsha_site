from django.shortcuts import render
from django.views.generic import TemplateView

from .models import ProjectCategory, Project, Employee, Skill, FrequentlyQuestion, Service, Subscriber
from .forms import MessageForm, SubscribeForm


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
        context['frequently_questions'] = FrequentlyQuestion.objects.filter(is_visible=True)
        context['services'] = Service.objects.filter(is_visible=True)

        return context

    def post(self, request, *args, **kwargs):
        form_id = request.POST.get('form_id')
        if form_id == 'messageForm':
            return send_message(request)
        elif form_id == 'subscribeForm':
            return send_subscribe(request)


def send_message(request):
    message_form = MessageForm(request.POST)
    if message_form.is_valid():
        message_form.save()
        message_form = MessageForm()
    return render(request, 'index.html', {'message_form': message_form})


def send_subscribe(request):
    subscribe_form = SubscribeForm(request.POST)
    if subscribe_form.is_valid():
        email = request.POST.get('email')
        username = request.user.username or 'Anonymous'
        subscriber = Subscriber.objects.create(email=email, username=username)
        subscriber.save()
    return render(request, 'index.html', {'subscribe_form': subscribe_form})
