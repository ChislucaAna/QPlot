# formulare pt creearea de noi plotturi
from django import forms
from .models.Points import Punct


class PointForm(forms.Form):
    x = forms.FloatField(label='X:',required=False)
    y = forms.FloatField(label='Y:',required=False)


class LineForm(forms.Form):
    x1 = forms.FloatField(label='X1:',required=False)
    y1 = forms.FloatField(label='Y1:',required=False)
    x2 = forms.FloatField(label='X2:',required=False)
    y2 = forms.FloatField(label='Y2:',required=False)


class FunctionForm(forms.Form):
    function = forms.CharField(label='f(x)', max_length=100, required=False)

class ConfigForm(forms.Form):
    startx = forms.FloatField(label='Left X', required=False)
    endx = forms.FloatField(label='Right X', required=False)