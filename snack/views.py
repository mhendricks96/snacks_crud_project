from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Snack
from django.urls import reverse_lazy
# Create your views here.

class HomeView(TemplateView):
  template_name = 'home.html'
  #model = Snack

class SnackListView(ListView):
  template_name = 'snack_list.html'
  model = Snack
  context_object_name = 'list_of_snacks'

class SnackDetailView(DetailView):
  template_name = 'snack_detail.html'
  model = Snack

class SnackCreateView(CreateView):
  template_name = 'create_snack.html'
  model = Snack
  fields = ['title', 'purchaser' ,'description']
  success_url = reverse_lazy('snack_list')

class SnackUpdateView(UpdateView):
  template_name = 'update_snack.html'
  model = Snack
  fields = ['title', 'purchaser', 'description']
  success_url = reverse_lazy('snack_list')

class SnackDeleteView(DeleteView):
  template_name = 'delete_snack.html'
  model = Snack
  success_url = reverse_lazy('snack_list')