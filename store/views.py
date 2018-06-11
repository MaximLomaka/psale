from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView

from store.forms import UserForm
from store.models import Advertisement


class AdListView(ListView):
    template_name = 'store/index.html'
    queryset = Advertisement.objects.all()


class AdDetailView(ListView):
    template_name = 'store/detail.html'
    model = Advertisement


class CreateUserView(FormView):
    form_class = UserForm
    template_name = 'store/registration.html'

    success_url = reverse_lazy('store:index')

    def form_valid(self, form):
        form.save(form)
        messages.success(self.request, 'user was created successfully')

        return super().form_valid(form)
