from django.views.generic import ListView

from store.models import Advertisement


class AdListView(ListView):
    template_name = 'store/index.html'
    queryset = Advertisement.objects.all()
