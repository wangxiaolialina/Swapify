from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.views.generic import ListView, DetailView

from .models import Clothing, Shoe, Photo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
def home(request):
    return render(request, 'home.html')


def clothings_index(request):
    clothings = Clothing.objects.all()
    return render(request, 'clothings/index.html', {'clothings': clothings})


@login_required
def myclothings_index(request):
    myclothings = Clothing.objects.filter(user=request.user)
    myshoes = Shoe.objects.filter(user=request.user)
    return render(request, 'clothings/myindex.html',
                  {'myclothings': myclothings,'myshoes': myshoes })


@login_required
def clothings_detail(request, clothing_id):
    clothing = Clothing.objects.get(id=clothing_id)
    # Get the toys the cat doesn't have
    #   toys_cat_doesnt_have = Toy.objects.exclude(id__in = cat.toys.all().values_list('id'))
    # Instantiate FeedingForm to be rendered in the template
    return render(
        request,
        'clothings/detail.html',
        {
            # Pass the cat and feeding_form as context
            'cloth': clothing,
            # Add the toys to be displayed
            # 'toys': toys_cat_doesnt_have
        })


class ClothingCreate(LoginRequiredMixin, CreateView):
    model = Clothing
    fields = ['name', 'category', 'brand', 'description', 'size']

    def form_valid(self, form):
        # Assign the logged in user
        form.instance.user = self.request.user
        # Let the CreateView do its job as usual
        return super().form_valid(form)


class ClothingUpdate(LoginRequiredMixin, UpdateView):
    model = Clothing
    fields = ['category', 'brand', 'description', 'size']


class ClothingDelete(LoginRequiredMixin, DeleteView):
    model = Clothing
    success_url = '/clothings/'


def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in via code
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


class ShoeList(ListView):
    model = Shoe


class ShoeDetail(LoginRequiredMixin, DetailView):
    model = Shoe


class ShoeCreate(LoginRequiredMixin, CreateView):
    model = Shoe
    fields = ['name', 'brand', 'color','shoe_size','description' ]

    def form_valid(self, form):
        # Assign the logged in user
        form.instance.user = self.request.user
        # Let the CreateView do its job as usual
        return super().form_valid(form)

