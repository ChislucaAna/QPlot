from django.shortcuts import redirect, get_object_or_404, render
from visualizerapp.models.Points import Punct
from visualizerapp.models.Lines import Line
import tkinter as tk

def line_info(request, line_id):
    if request.method == 'POST':
        lines = request.session.get('lines', [])
        l =lines[line_id]
        #lines ar stored in session as dict
        # we need to convert them back to Line instaces
        #to accces class methods
        p1 =Punct(l['p1']['x'], l['p1']['y'])
        p2= Punct(l['p2']['x'], l['p2']['y'])
        new_line = Line(p1, p2)
        print(new_line.lungime())
        return redirect('plotter')