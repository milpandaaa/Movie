from django.contrib.auth import authenticate, login
from django.http import Http404
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import *


def base(request):
    context = {'data_c': Сassette.objects.all(), 'data_s': Seller.objects.all(), 'data_a': Admission.objects.all(), 'data_t':Сassette.objects.values('theme').distinct()}
    return render(request, 'base.html', context)


def sort(request, theme):
    context = {'data_c': Сassette.objects.all().filter(theme__exact=theme), 'data_s': Seller.objects.all(), 'data_a': Admission.objects.all()}
    return render(request, 'sort.html', context)


def search(request):
    context = {'data_c': Сassette.objects.all()}
    return render(request, 'search.html', context)


def account(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
        context = {'data_u': user, 'data_c': Сassette.objects.all(), 'data_s': Seller.objects.all(),
                   'data_sg': Selling.objects.all()}
    except User.DoesNotExist:
        raise Http404("Пользователя не сущетсвует")
    return render(request, 'account.html', context)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.photo = form.cleaned_data.get('photo')
            user.save()
            my_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=my_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
        return render(request, 'signup.html', {'form': form})


def selling(request, user_id, cassette_id):
    context = {}
    form = Selling_form(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    context['data_u'] = User.objects.get(pk=user_id)
    context['data_c'] = Сassette.objects.get(pk=cassette_id)
    context['data_s'] = Seller.objects.all()
    context['data_a'] = Admission.objects.all()
    context['form'] = form
    return render(request, "selling.html", context)


def cassetteAdd(request):
    context = {}
    form = Сassette_form(request.POST or None)
    context['data_c'] = Сassette.objects.all()
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "cassetteAdd.html", context)


def sellerAdd(request):
    context = {}
    form = Seller_form(request.POST or None)
    context['data_c'] = Seller.objects.all()
    if form.is_valid():
        form.save()
        return render(request, "sellers.html", context)
    context['form'] = form
    return render(request, "sellerAdd.html", context)


def sellers(request):
    context = {'data_c': Seller.objects.all()}
    return render(request, 'sellers.html', context)


def cassetteDelete(request, cassette_id):
    try:
        c = Сassette.objects.get(id=cassette_id)
        c.delete()
        return redirect('/')
    except Сassette.DoesNotExist:
        return HttpResponseNotFound("<h2>Фильм не найден</h2>")


def forDelete(request):
    context = {'data_c': Сassette.objects.all()}
    return render(request, 'cassetteDelete.html', context)


def sellerDelete(request, seller_id):
    try:
        c = Seller.objects.get(id=seller_id)
        c.delete()
        return redirect('/')
    except Сassette.DoesNotExist:
        return HttpResponseNotFound("<h2>Продавец не найден</h2>")


def admissionAdd(request, seller_id):
    context = {}
    form = Admission_form(request.POST or None)
    context['data_a'] = Admission.objects.all()
    context['seller'] = seller_id
    context['data_c'] = Сassette.objects.all()
    if form.is_valid():
        form.save()
        context['data_c'] = Seller.objects.all()
        return render(request, "sellers.html", context)
    context['form'] = form
    return render(request, "admissionAdd.html", context)
