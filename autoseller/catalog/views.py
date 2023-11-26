from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .models import Cars, TestDrive
from django.views.generic import DetailView, UpdateView, DeleteView
from .forms import CarsForm, TestDriveForm


def catalog(request):
    choice = 'price'
    if request.method == "POST":
        choice = request.POST.get('choice')
    else:
        choice_param = request.GET.get('choice')

        if choice_param == 'choice1':
            choice = '-price'
        elif choice_param == 'choice2':
            choice = 'price'
        elif choice_param == 'choice3':
            choice = '-date'
        elif choice_param == 'choice4':
            choice = 'date'

    cars = Cars.objects.order_by(choice)
    return render(request, 'catalog/catalog.html', {'cars': cars})


class AutoDetailView(LoginRequiredMixin, DetailView):
    model = Cars
    template_name = 'catalog/details_view.html'
    context_object_name = 'car'
    login_url = 'login'  # detail viewing only for authenticated users (закинуть в url для оформления тест-драйва)


def create(request):
    errors = []
    if request.method == 'POST':
        car_form = CarsForm(request.POST, request.FILES)  # добавить encrypte в тэг формы
        if car_form.is_valid():
            car_form.save()
            return redirect('catalog')
        else:
            errors = car_form.errors.values()

    car_form = CarsForm

    return render(request, 'catalog/add_car.html', {'car_form': car_form, 'errors': errors})


class AutoUpdateView(UpdateView):
    model = Cars
    template_name = 'catalog/edit_car.html'
    form_class = CarsForm  # absolute_url in models.py
    # add errors


class AutoDeleteView(DeleteView):
    model = Cars
    success_url = '/catalog'
    template_name = 'catalog/delete_car.html'


@login_required
def testdrive(request, car_id):
    car = get_object_or_404(Cars, pk=car_id)
    user = request.user
    errors = []
    if request.method == 'POST':  # забыл .method
        testdrive_form = TestDriveForm(request.POST, initial={'car': car, 'user': user})
        if testdrive_form.is_valid():
            testdrive = testdrive_form.save(commit=False)  # сохранить но не записывать в БД
            testdrive.car = car
            testdrive.save()
            return redirect('profile')
        else:
            errors = testdrive_form.errors.values()

    testdrive_form = TestDriveForm(initial={'car': car, 'user': user})
    return render(request, 'catalog/testdrive.html', {'testdrive_form': testdrive_form, 'errors': errors, 'car': car})

# добавить в ЛК пользователя его тест-драйвы
