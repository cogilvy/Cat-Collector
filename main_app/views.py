from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Cat, Toy
from .forms import FeedingForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# View functions

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def cats_index(request):
  cats = Cat.objects.filter(user=request.user)
  # cats = request.user.cat_set.all()
  return render(request, 'cats/index.html', { 'cats': cats })

@login_required
def cats_detail(request, cat_id):
  cat = Cat.objects.get(id=cat_id)
  if cat.user == request.user:
    # instantiate FeedingForm to be rendered in the detail.html template
    feeding_form = FeedingForm()
    # find all toys not associated with this cat
    toys_cat_doesnt_have = Toy.objects.exclude(id__in=cat.toys.all().values_list('id'))
    return render(request, 'cats/detail.html', {
      'cat': cat,
      'feeding_form': feeding_form,
      'toys': toys_cat_doesnt_have
    })
  else:
    return redirect('cats_index')


class CatCreate(LoginRequiredMixin, CreateView):
  model = Cat
  fields = ['name', 'breed', 'description', 'age']

  def form_valid(self, form):
    # Assign the logged in user as owner of the Cat being created
    form.instance.user = self.request.user
    # Let the CreateView do its job as usual
    return super().form_valid(form)


class CatUpdate(LoginRequiredMixin, UpdateView):
  model = Cat
  fields = ['breed', 'description', 'age']


class CatDelete(LoginRequiredMixin, DeleteView):
  model = Cat
  success_url = '/cats/'

@login_required
def add_feeding(request, cat_id):
  # create a ModelForm instance using the data in the posted form
  form = FeedingForm(request.POST)
  # validate the data
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.cat_id = cat_id
    new_feeding.save()
  return redirect('cats_detail', cat_id=cat_id)


class ToyList(LoginRequiredMixin, ListView):
  model = Toy


class ToyDetail(LoginRequiredMixin, DetailView):
  model = Toy


class ToyCreate(LoginRequiredMixin, CreateView):
  model = Toy
  fields = '__all__'


class ToyUpdate(LoginRequiredMixin, UpdateView):
  model = Toy
  fields = ['name', 'color']


class ToyDelete(LoginRequiredMixin, DeleteView):
  model = Toy
  success_url = '/toys/'

@login_required
def assoc_toy(request, cat_id, toy_id):
  cat = Cat.objects.get(id=cat_id)
  cat.toys.add(toy_id)
  return redirect('cats_detail', cat_id=cat_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('cats_index')
    else:
      error_message = 'Invalid sign up - try again!'

  form = UserCreationForm()
  context = {
    'form': form,
    'error_message': error_message
  }
  return render(request, 'registration/signup.html', context)
  
