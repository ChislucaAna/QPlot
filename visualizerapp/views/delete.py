from django.shortcuts import redirect, get_object_or_404, render
from visualizerapp.models.Points import Punct
from visualizerapp.models.Lines import Line

def delete_line(request, line_id):
    if request.method == 'POST':
        lines = request.session.get('lines', [])
        #scot linia cu indexu ala
        lines = [line for idx, line in enumerate(lines) if idx != int(line_id)]
        request.session['lines'] = lines
        request.session.modified = True
        return redirect('plotter')

def delete_point(request, point_id):
    if request.method == 'POST':
        points = request.session.get('points', [])
        #scot punctul cu indexu ala
        points = [point for idx, point in enumerate(points) if idx != int(point_id)]
        request.session['points'] = points
        request.session.modified = True
        return redirect('plotter')

