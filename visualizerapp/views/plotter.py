from django.shortcuts import render, redirect
from django.views import View
# Forms for creating geometric elements
from visualizerapp.forms import PointForm, LineForm
from visualizerapp.models.Points import Punct
from visualizerapp.models.Lines import Line
#serializers
from visualizerapp.serializers import PunctSerializer, LineSerializer
#plotting methods:
from visualizerapp.plotter_methods.plotter_methods import *
from visualizerapp.views.delete import delete_line

class PlotView(View):
    def get(self, request, *args, **kwargs):
        #init session
        self.initialize_session(request)

        #init forms
        point_form=PointForm()
        line_form=LineForm()
        #current session context for data load
        context_data = self.get_session_data(request)
        context = self.create_context(request, point_form, line_form,context_data)
        #plot with current context
        request.session['plot_url']= generate_plot_url(self.get_session_data(request))
        #update context post-plot
        context_data = self.get_session_data(request)
        context = self.create_context(request, point_form, line_form,context_data)
        return render(request, 'plotter.html', context)

    def post(self, request, *args, **kwargs):

        point_form = PointForm(request.POST or None)
        line_form = LineForm(request.POST or None)

        context_data = self.get_session_data(request)

        #post requests:
        if 'connect_points' in request.POST:
            request.session['connect_points'] = not context_data['connect_points']
        elif 'show_middles' in request.POST:  
            request.session['show_middles'] = not context_data['show_middles']
        elif 'show_intersection' in request.POST:
            request.session['show_intersection'] = not context_data['show_intersection']
        elif 'show_length' in request.POST:  
            request.session['show_length'] = not context_data['show_length']
        elif 'show_slope' in request.POST:
            request.session['show_slope'] = not context_data['show_slope']
        elif 'add_point' in request.POST:
            if point_form.is_valid():
                x = point_form.cleaned_data['x']
                y = point_form.cleaned_data['y']
                new_point = Punct(float(x),float(y))
                serialized_point=PunctSerializer(new_point).data
                context_data['points'].append(serialized_point)
                request.session['points'] = context_data['points']
        elif'add_line' in request.POST:
            if line_form.is_valid():
                x1= line_form.cleaned_data['x1']
                y1 = line_form.cleaned_data['y1']
                x2 = line_form.cleaned_data['x2']
                y2 = line_form.cleaned_data['y2']
                p1 = Punct(float(x1),float(y1))
                p2 = Punct(float(x2),float(y2))
                new_line = Line(p1, p2)
                serialized_line = LineSerializer(new_line).data
                context_data['lines'].append(serialized_line) 
                request.session['lines'] = context_data['lines']  
        request.session.modified = True
        #plot with current context
        request.session['plot_url']= generate_plot_url(self.get_session_data(request))
        #update context post-plot
        context_data=self.get_session_data(request)
        context = self.create_context(request, point_form, line_form, context_data)
        return render(request, 'plotter.html', context)

    def create_context(self, request, point_form, line_form, context_data):
        return {
            'connect_points': context_data['connect_points'],
            'show_middles': context_data['show_middles'],
            'show_intersection': context_data['show_intersection'],
            'show_length': context_data['show_length'],
            'show_slope': context_data['show_slope'],
            'line_form': line_form,
            'point_form': point_form,
            'plot_url': context_data['plot_url'],
            'points': context_data['points'],
            'lines': context_data['lines'],
        }
    
    def initialize_session(self, request):
        if 'points' not in request.session:
            request.session['points'] = []
        if 'lines' not in request.session:
            request.session['lines'] = []

    
    def get_session_data(self, request):
        return {
            'connect_points': request.session.get('connect_points'),
            'show_middles': request.session.get('show_middles'),
            'show_intersection': request.session.get('show_intersection'),
            'show_length': request.session.get('show_length'),
            'show_slope': request.session.get('show_slope'),
            'points': request.session.get('points', []),
            'lines': request.session.get('lines', []),
            'plot_url': request.session.get('plot_url'),
        }
