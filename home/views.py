import os
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView

from .forms import ContactForm, PayForm
from .models import Car, Basket, PayModel


def pay(request, id):
    error = ''
    if request.method == 'POST':
        form = PayForm(request.POST)
        if form.is_valid():
            response = form.save(commit=False)
            response.user = request.user
            response.product_id = id
            form.save()
            return redirect(reverse_lazy('pay_success'))
        else:
            error = 'Error'
    form = PayForm()

    data = {
        'form': form,
        'error': error,
        'id': id,
    }

    return render(request, 'home/pay.html', data)


def pay_success(requset):
    return render(requset, 'home/pay_messege.html')


def about(request):
    return render(request, 'home/about.html')


@login_required(login_url='login')
def callform(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Пробное сообщение"
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())
            try:
                send_mail(subject, message,
                          os.getenv('EMAIL'),
                          [os.getenv('EMAIL')])
            except BadHeaderError:
                return HttpResponse('Найден некорректный заголовок')
            return redirect("success_callform")

    form = ContactForm()
    return render(request, "home/callform.html", {'form': form})


@login_required(login_url='login')
def success_callform(request):
    return render(request, 'home/success_callform.html')


# def new_matiz(request):
#     matiz = Car.objects.all()
#     return render(request, 'home/new_matiz.html', {'matiz': matiz})


class NewListMatiz(ListView):
    template_name = 'home/new_matiz.html'
    model = Car
    context_object_name = 'matiz'
    paginate_by = 2


class NewSearchList(NewListMatiz):
    paginate_by = 2

    def get_queryset(self):
        return Car.objects.filter(name__icontains=self.request.GET.get('search_new', ''))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['search_new'] = self.request.GET.get('search_new')
        return context


class ListMatiz(ListView):
    template_name = 'home/index.html'
    model = Car
    context_object_name = 'matiz'
    paginate_by = 3


class SearchList(ListMatiz):
    paginate_by = 3

    def get_queryset(self):
        return Car.objects.filter(name__icontains=self.request.GET.get('search', ''))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['search'] = self.request.GET.get('search')
        return context


class MatizDetailView(DetailView):
    model = Car
    template_name = 'home/detail.html'
    context_object_name = 'matizz'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


@login_required(login_url='login')
def basket(request, id):
    if id == request.user.id:
        product = Basket.objects.filter(user=request.user)
        return render(request, 'home/basket.html', {'product': product, 'id': id})
    else:
        return HttpResponseNotFound('<h1>Страница не найдена</h1>')


@login_required(login_url='login')
def basket_add(request, matiz_id):
    product = Car.objects.get(id=matiz_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        basket = Basket(user=request.user, product=product)
        basket.save()
        return redirect(reverse_lazy('basket', args=[request.user.pk]))
    else:
        return redirect(reverse_lazy('basket', args=[request.user.pk]))


@login_required(login_url='login')
def basket_delete(request, id):
    basket = Basket.objects.get(id=id)
    basket.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
