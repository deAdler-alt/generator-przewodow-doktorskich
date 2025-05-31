from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Doktorat
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class DoktoratListView(ListView):
    model = Doktorat
    template_name = 'core/doktorat_list.html'

@method_decorator(login_required, name='dispatch')
class DoktoratDetailView(DetailView):
    model = Doktorat
    template_name = 'core/doktorat_detail.html'

@method_decorator(login_required, name='dispatch')
class DoktoratCreateView(CreateView):
    model = Doktorat
    fields = ['doktorant', 'tytul', 'promotor', 'promotorPomocniczy', 'kopromotor', 'rozprawa', 'komentarz']
    template_name = 'core/doktorat_form.html'
    success_url = reverse_lazy('doktorat_list')

@method_decorator(login_required, name='dispatch')
class DoktoratUpdateView(UpdateView):
    model = Doktorat
    fields = ['doktorant', 'tytul', 'promotor', 'promotorPomocniczy', 'kopromotor', 'rozprawa', 'komentarz']
    template_name = 'core/doktorat_form.html'
    success_url = reverse_lazy('doktorat_list')

@method_decorator(login_required, name='dispatch')
class DoktoratDeleteView(DeleteView):
    model = Doktorat
    template_name = 'core/doktorat_confirm_delete.html'
    success_url = reverse_lazy('doktorat_list')
