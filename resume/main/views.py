from django.shortcuts import get_list_or_404, get_object_or_404, redirect
from django.views.generic import DetailView
from django.db.models import F
from django.conf import settings
from django.core.mail import send_mail


from .models import *


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        recipient = Contact.objects.get(candidate_id=settings.DEFAULT_CANDIDATE, type=Contact.TypeConnect.EMAIL)

        mail = send_mail(
            f'{name} откликнулся на резюме',
            f'{message}\n\nПочта для связи: {email}',
            settings.EMAIL_HOST_USER,
            [recipient.connect])

    if not mail:
        raise

    return redirect('home')


class Home(DetailView):
    model = Candidate
    template_name = 'main/index.html'
    context_object_name = 'candidate'

    def get_object(self, queryset=None):
        return get_object_or_404(Candidate, pk=settings.DEFAULT_CANDIDATE)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contacts'] = get_list_or_404(Contact, candidate_id=self.object.pk)
        context['experience'] = get_list_or_404(Experience, candidate_id=self.object.pk)
        context['education'] = get_list_or_404(Education, candidate_id=self.object.pk)
        context['certificates'] = get_list_or_404(Certificate, candidate_id=self.object.pk)
        context['hardskill'] = get_list_or_404(HardSkill, candidate_id=self.object.pk)
        context['softskill'] = get_list_or_404(SoftSkill, candidate_id=self.object.pk)
        self.object.views = F('views') + 1
        self.object.save()
        self.object.refresh_from_db()
        return context
