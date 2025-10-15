from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Product
from .forms import ProductForm

class TradersListView(ListView):
  model = Product
  template_name='traders/index.html'
  context_object_name="products"

class TradersDetailView(DetailView):
  model = Product
  template_name = 'traders/detail.html'
  context_object_name = "detailedProduct"

class TradersCreateView(CreateView):
  model = Product
  form_class = ProductForm
  success_url = '/traders'
    
class TradersUpdateView(UpdateView):
  model = Product
  form_class = ProductForm
  success_url = '/traders'

class TradersDeleteView(DeleteView):
  model = Product
  success_url = '/traders'
  template_name = 'traders/delete.html'