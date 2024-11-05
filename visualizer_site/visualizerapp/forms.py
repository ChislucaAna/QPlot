# formulare pt creearea de noi plotturi
from django import forms
from .models.Points import Punct

class PointForm(forms.Form):
    x = forms.FloatField(label='X Coordinate')
    y = forms.FloatField(label='Y Coordinate')

class TriunghiForm(forms.Form):
    A = forms.FloatField(label='Frist Point')
    B = forms.FloatField(label='Second Point')
    C = forms.FloatField(label='Third Point')
