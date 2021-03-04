from django import forms
from django.forms import widgets

from webapp.models import status_choices

class TaskForm(forms.Form):
    description = forms.CharField(max_length=160, required=True, label='Описание')
    text = forms.CharField(max_length=1500, required=False, widget=widgets.Textarea, label='Подробнее о задаче')
    status = forms.ChoiceField(choices=status_choices, required=True, label='Статус')
    date = forms.DateField(required=False, widget=widgets.DateInput, label='Дата (в формате ГГГГ-мм-дд)')