from django.shortcuts import redirect, get_object_or_404, render
from visualizerapp.models.Points import Punct
from visualizerapp.models.Lines import Line
import tkinter as tk

from visualizerapp.serializers import LineSerializer

def line_info(request, line_id):
    if request.method == 'POST':
        lines = request.session.get('lines', [])
        l =lines[line_id]
        #lines ar stored in session as dict
        # we need to convert them back to Line instaces
        #to accces class methods
        p1 =Punct(l['p1']['x'], l['p1']['y'])
        p2= Punct(l['p2']['x'], l['p2']['y'])
        line = Line(p1, p2)
        line_info = request.session.get('line_info', {})
        line_info["length"] = line.lungime()
        line_info["slope"] = line.panta()
        line_info["mediatoare"]=LineSerializer(line.mediatoare()).data
        request.session.modified = True
        return redirect('plotter')