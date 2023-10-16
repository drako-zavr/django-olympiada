from django import forms

from django.forms import ModelForm
from .models import Registration


# class RegForm(forms.Form):
#     fio = forms.CharField(label= "ФИО", max_length=150)
#     university = forms.CharField(label= "Наименование учебного заведения",max_length=200)
#     tel = forms.CharField(label= "Телефон", max_length=11)
#     email = forms.CharField(label= "Email", max_length=255)



class RegForm(ModelForm):
    # ?????????
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'registration-form__input'
            visible.field.widget.attrs['placeholder'] = visible.field.label

    class Meta:
        model = Registration
        #fields = '__all__'
        fields = ["fio", "university", "tel", "email"]


