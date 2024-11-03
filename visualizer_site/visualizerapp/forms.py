# formulare pt creearea de noi plotturi
from django import forms

class PointForm(forms.Form):
    x = forms.FloatField(label='X Coordinate')
    y = forms.FloatField(label='Y Coordinate')
