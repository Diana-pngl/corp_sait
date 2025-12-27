from django import forms 
from corp_sait import models
class Forma_dlia_cozdania_e(forms.ModelForm):
    class Meta:
        model = models.Event
        fields = ['name','guests','budget','description','date'] 

class Forma_dlia_coedinenia_k(forms.Form):
    team = forms.ModelChoiceField(queryset=models.Team.objects.all(), label="Выберите команду")
    event = forms.ModelChoiceField(queryset=models.Event.objects.all(), label="Выберите событие")