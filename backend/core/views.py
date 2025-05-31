from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Doktorat

class DoktoratListView(ListView):
    model = Doktorat
    template_name = 'core/doktorat_list.html'

class DoktoratDetailView(DetailView):
    model = Doktorat
    template_name = 'core/doktorat_detail.html'

class DoktoratCreateView(CreateView):
    model = Doktorat
    fields = ['doktorant', 'tytul', 'promotor', 'promotorPomocniczy', 'kopromotor', 'rozprawa', 'komentarz']
    template_name = 'core/doktorat_form.html'
    success_url = reverse_lazy('doktorat_list')

class DoktoratUpdateView(UpdateView):
    model = Doktorat
    fields = ['doktorant', 'tytul', 'promotor', 'promotorPomocniczy', 'kopromotor', 'rozprawa', 'komentarz']
    template_name = 'core/doktorat_form.html'
    success_url = reverse_lazy('doktorat_list')

class DoktoratDeleteView(DeleteView):
    model = Doktorat
    template_name = 'core/doktorat_confirm_delete.html'
    success_url = reverse_lazy('doktorat_list')
