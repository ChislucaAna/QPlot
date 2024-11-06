# formulare pt creearea de noi plotturi
from django import forms
from .models.Points import Punct

class PointForm(forms.Form):
    x = forms.FloatField(label='X Coordinate')
    y = forms.FloatField(label='Y Coordinate')

class LineForm(forms.Form):
    x1 = forms.FloatField(label='X Coordinate of First Point')
    y1 = forms.FloatField(label='Y Coordinate of First Point')
    x2 = forms.FloatField(label='X Coordinate of Second Point')
    y2 = forms.FloatField(label='Y Coordinate of Second Point')
