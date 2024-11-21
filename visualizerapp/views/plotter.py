from django.shortcuts import render, redirect
from django.views import View
# Forms for creating geometric elements
from visualizerapp.forms import PointForm, LineForm
from visualizerapp.models.Points import Punct
from visualizerapp.models.Lines import Line
#serializers
from visualizerapp.serializers import PunctSerializer, LineSerializer
#plotting methods:
from visualizerapp.plotter_methods.plot_points import plot_points
from visualizerapp.plotter_methods.plot_lines import plot_lines
from visualizerapp.plotter_methods.config_visuals import config

def serialize_points(points):
    return [PunctSerializer(point).data for point in points]

def serialize_lines(lines):
    return [LineSerializer(line).data for line in lines]

class PlotView(View):
    def get(self, request, *args, **kwargs):

        #create session specific data storage
        if 'points' not in request.session:
            request.session['points'] = []
        if 'lines' not in request.session:
            request.session['lines'] = []
        
        #initialize forms
        point_form=PointForm()
        line_form=LineForm()

        #current session context for data load
        context = {
            'connect_points':request.session.get('connect_points', False),
            'show_middles':request.session.get('show_middles', False),
            'show_intersection':request.session.get('show_intersection', False),
            'line_form':line_form,
            'point_form': point_form, 
            'plot_url': request.session.get('plot_url'),
            'points': request.session['points'],
            'lines':request.session['lines'],
        }
        return render(request, 'plotter.html', context)

    def post(self, request, *args, **kwargs):
        #initialize post-request specific forms
        point_form = PointForm(request.POST or None)
        line_form = LineForm(request.POST or None)

        #request session data
        points = request.session.get('points', [])
        lines = request.session.get('lines', [])
        connect_points = request.session.get('connect_points', False)
        show_middles = request.session.get('show_middles', False)
        show_intersection=request.session.get('show_intersection', False)


        #post requests:
        if 'connect_points' in request.POST:
            request.session['connect_points'] = not connect_points
        if 'show_middles' in request.POST:  
            request.session['show_middles'] = not show_middles
        if 'show_intersection' in request.POST:  
            request.session['show_intersection'] = not show_intersection
        elif 'add_point' in request.POST:
            if point_form.is_valid():
                x = point_form.cleaned_data['x']
                y = point_form.cleaned_data['y']
                new_point = Punct(x,y)
                serialized_point=PunctSerializer(new_point).data
                points.append(serialized_point)
        elif 'add_line' in request.POST:
            if line_form.is_valid():
                x1= line_form.cleaned_data['x1']
                y1 = line_form.cleaned_data['y1']
                x2 = line_form.cleaned_data['x2']
                y2 = line_form.cleaned_data['y2']
                p1 = Punct(x1, y1)
                p2 = Punct(x2, y2)
                new_line = Line(p1, p2)
                serialized_line = LineSerializer(new_line).data
                lines.append(serialized_line)

        elif 'plot_points' in request.POST:
            config()
            plot_url = plot_points(points,connect_points)
            request.session['plot_url'] = plot_url
        
        elif 'plot_lines' in request.POST:
            config()
            plot_url = plot_lines(lines,show_intersection,show_middles)
            request.session['plot_url'] = plot_url
        
        # update session data
        request.session['points'] = points
        request.session['lines'] = lines
        request.session.modified = True

        context = {
            'connect_points':request.session.get('connect_points', False),
            'show_middles':request.session.get('show_middles', False),
            'show_intersection':request.session.get('show_intersection', False),
            'line_form':line_form,
            'point_form': point_form, 
            'plot_url': request.session.get('plot_url'),
            'points': request.session['points'],
            'lines':request.session['lines'],
        }
        return render(request, 'plotter.html', context)
