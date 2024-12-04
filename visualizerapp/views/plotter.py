from django.shortcuts import render, redirect
from django.views import View
# Forms for creating geometric elements
from visualizerapp.forms import *
#serializers
from visualizerapp.serializers import PunctSerializer, LineSerializer
#plotting methods:
from visualizerapp.plotter_methods.plotter_methods import *
#model for saving plot into db
from visualizerapp.models.project_context import ProjectContext

class PlotView(View):
    def get(self, request,*args, **kwargs):
        id = request.GET.get('id')
        context_data = self.get_context_data(id)
        self.initialize_session(request, context_data)
        point_form=PointForm()
        line_form=LineForm()
        func_form=FunctionForm()
        config_form=ConfigForm()
        context=self.plot_and_update_context(request,point_form,line_form,func_form,config_form)
        return render(request, 'plotter.html', context)

    def post(self, request,*args, **kwargs):
        point_form=PointForm(request.POST or None)
        line_form = LineForm(request.POST or None)
        func_form = FunctionForm(request.POST or None)
        config_form = ConfigForm(request.POST or None)
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
            self.add_point(request,point_form,context_data)
        elif 'add_line' in request.POST:
            self.add_line(request,line_form,context_data)
        elif 'add_function' in request.POST:
            self.add_function(request,func_form,context_data)
        elif 'save' in request.POST:
            self.save_project(request)

        request.session.modified = True
        context = self.plot_and_update_context(request, point_form, line_form, func_form, config_form)
        return render(request, 'plotter.html', context)

    def add_point(self,request,point_form,context_data):
        if point_form.is_valid():
            x = point_form.cleaned_data['x']
            y = point_form.cleaned_data['y']
            new_point = Punct(float(x), float(y))
            serialized_point = PunctSerializer(new_point).data
            context_data['points'].append(serialized_point)
            request.session['points'] = context_data['points']

    def add_line(self, request, line_form, context_data):
        if line_form.is_valid():
            x1 = line_form.cleaned_data['x1']
            y1 = line_form.cleaned_data['y1']
            x2 = line_form.cleaned_data['x2']
            y2 = line_form.cleaned_data['y2']
            p1 = Punct(float(x1), float(y1))
            p2 = Punct(float(x2), float(y2))
            new_line = Line(p1, p2)
            serialized_line = LineSerializer(new_line).data
            context_data['lines'].append(serialized_line)
            request.session['lines'] = context_data['lines']

    def add_function(self, request, func_form, context_data):
        if func_form.is_valid():
            func = func_form.cleaned_data['function']
            context_data['functions'].append(func)
            request.session['functions'] = context_data['functions']
        else:
            print("invalid form")

    def plot_and_update_context(self, request, point_form, line_form, func_form,config_form):
        request.session['plot_url'] = generate_plot_url(self.get_session_data(request))
        # update context post-plot
        context_data = self.get_session_data(request)
        context = self.create_context(request, point_form, line_form,func_form, config_form,context_data)
        return context

    def create_context(self, request, point_form, line_form,func_form,config_form, context_data):
        return {
            'connect_points': context_data['connect_points'],
            'show_middles': context_data['show_middles'],
            'show_intersection': context_data['show_intersection'],
            'show_length': context_data['show_length'],
            'show_slope': context_data['show_slope'],
            'line_form': line_form,
            'point_form': point_form,
            'func_form': func_form,
            'config_form': config_form,
            'plot_url': context_data['plot_url'],
            'points': context_data['points'],
            'lines': context_data['lines'],
            'line_info': context_data['line_info'],
            'functions': context_data['functions']
        }
    
    def initialize_session(self, request,context_data=None):
        if context_data:
            request.session['connect_points'] = context_data.get('connect_points', False)
            request.session['show_middles'] = context_data.get('show_middles', False)
            request.session['show_intersection'] = context_data.get('show_intersection', False)
            request.session['show_length'] = context_data.get('show_length', False)
            request.session['show_slope'] = context_data.get('show_slope', False)
            request.session['points'] = context_data.get('points', [])
            request.session['lines'] = context_data.get('lines', [])
            request.session['functions'] = context_data.get('functions', [])
            request.session['line_info'] = context_data.get('line_info', {})
            request.session['plot_url'] = context_data.get('plot_url', None)
        else:
            if 'points' not in request.session:
                request.session['points'] = []
            if 'lines' not in request.session:
                request.session['lines'] = []
            if 'functions' not in request.session:
                request.session['functions'] = []
            if 'line_info' not in request.session:
                request.session['line_info'] = {}

    def get_context_data(self, id):
        # Fetch the context data for the project (if id is provided)
        try:
            project = ProjectContext.objects.get(id=id)
            context_data = project.context_data
        except ProjectContext.DoesNotExist:
            context_data = None
        return context_data

    def get_session_data(self, request,id=None):
        if id:
            context_data = self.get_context_data(id)  # Fetch the project data based on the id
            return context_data
        return {
            'connect_points': request.session.get('connect_points'),
            'show_middles': request.session.get('show_middles'),
            'show_intersection': request.session.get('show_intersection'),
            'show_length': request.session.get('show_length'),
            'show_slope': request.session.get('show_slope'),
            'points': request.session.get('points', []),
            'lines': request.session.get('lines', []),
            'functions':request.session.get('functions',[]),
            'plot_url': request.session.get('plot_url'),
            'line_info': request.session.get('line_info',{})
        }

    def save_project(self, request):
        if not request.user.is_authenticated:
            return redirect('login')
        context_data = self.get_session_data(request)
        # Save the data in the database
        project_context =  ProjectContext.objects.create(
            user=request.user,
            context_data=context_data)
        print(f"Project saved with ID: {project_context.id}")
