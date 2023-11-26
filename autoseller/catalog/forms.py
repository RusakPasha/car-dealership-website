from django.contrib.auth.models import User

from .models import Cars, TestDrive
from django.forms import ModelForm
from django import forms
import datetime
from django.core.exceptions import ValidationError
from django.utils import timezone


class CarsForm(ModelForm):
    brand = forms.CharField(label="Марка", widget=forms.TextInput(attrs={'class': 'forms-input'}), required=False)
    model = forms.CharField(label="Модель", widget=forms.TextInput(attrs={'class': 'forms-input'}), required=False)
    price = forms.FloatField(label="Цена", widget=forms.NumberInput(attrs={'class': 'forms-input'}), required=False)
    date = forms.DateField(label="Дата выпуска", widget=forms.DateInput(attrs={'class': 'forms-input'}), required=False)
    img = forms.ImageField(label="Фото", widget=forms.FileInput(attrs={'class': 'forms-input'}), required=False)
    mileage = forms.IntegerField(label="Пробег", widget=forms.NumberInput(attrs={'class': 'forms-input'}),
                                 required=False)
    engine = forms.FloatField(label="Объем двигателя", widget=forms.NumberInput(attrs={'class': 'forms-input'}),
                              required=False)
    color = forms.CharField(label="Цвет", widget=forms.TextInput(attrs={'class': 'forms-input'}), required=False)

    class Meta:
        model = Cars
        fields = ['brand', 'model', 'price', 'date', 'img', 'fuel', 'mileage', 'engine', 'body_type', 'gear',
                  'drive_type', 'color']


class TestDriveForm(ModelForm):
    test_date = forms.DateField(label="Дата тест-драйва:", widget=forms.DateInput(attrs={'class': 'forms-input'}))
    duration = forms.IntegerField(label="Продолжительность:", widget=forms.NumberInput(attrs={'class': 'forms-input'}))
    car = forms.ModelChoiceField(label=" ", queryset=Cars.objects.all(), widget=forms.HiddenInput())
    user = forms.ModelChoiceField(label=" ", queryset=User.objects.all(), widget=forms.HiddenInput())

    def clean_test_date(self):
        test_date = self.cleaned_data['test_date']
        today = timezone.now().date()
        one_year_from_today = today + timezone.timedelta(days=365)
        if test_date < datetime.date.today():
            raise ValidationError("Невозможная дата!")
        elif test_date > one_year_from_today:
            raise ValidationError("Запись возможно только на следующие 365 дней!")
        return test_date

    def clean_duration(self):
        duration = self.cleaned_data['duration']
        if duration < 1 or duration > 12:
            raise ValidationError("Продолжительность от 1 до 12 часов!")
        return duration

    def clean(self):
        cleaned_data = super().clean()
        test_date = cleaned_data.get('test_date')
        car = cleaned_data.get('car')

        if car and test_date:
            existing_test_drives = TestDrive.objects.filter(car=car, test_date=test_date)

            if existing_test_drives.exists():
                raise ValidationError("Автомобиль забронирован на эту дату!")

    class Meta:
        model = TestDrive
        fields = ['test_date', 'duration', 'car', 'user']
