from django.shortcuts import render, redirect
from django.views import View
import matplotlib
matplotlib.use('Agg')  # Fixing: UserWarning: Starting a Matplotlib GUI outside of the main thread will likely fail.
import matplotlib.pyplot as plt  # plotting module
import io
import base64
# Forms for creating geometric elements
from visualizerapp.forms import PointForm, LineForm
from visualizerapp.models.Points import Punct
from visualizerapp.models.Lines import Line

# Storage variables for geometric elements 
points = []
lines=[]
plot_url=None
is_checked=False

class PlotView(View):
    def get(self, request, *args, **kwargs):
        global plot_url
        global is_checked
        point_form=PointForm()
        line_form=LineForm()
        context = {
            'is_checked':is_checked,
            'line_form':line_form,
            'point_form': point_form, 
            'plot_url': plot_url,  # URL for the img (null initially)
            'points': points,  # List of points created so far
            'lines':lines,
        }
        return render(request, 'plotter.html', context)

    def post(self, request, *args, **kwargs):
        global plot_url
        global points
        global lines
        global is_checked
        point_form=PointForm()
        line_form=LineForm()

        if 'connect_points' in request.POST:
            is_checked = not is_checked
        elif 'add_line' in request.POST:
            line_form = LineForm(request.POST)
            if line_form.is_valid():
                x1= line_form.cleaned_data['x1']
                y1 = line_form.cleaned_data['y1']
                x2 = line_form.cleaned_data['x2']
                y2 = line_form.cleaned_data['y2']
                lines.append(Line(Punct(x1,y1),Punct(x2,y2)))
        elif 'add_point' in request.POST:  # Add point button was clicked
            point_form = PointForm(request.POST)
            if point_form.is_valid():
                # Django forms validate data automatically and it is added to cleaned_data
                x = point_form.cleaned_data['x']
                y = point_form.cleaned_data['y']
                points.append(Punct(x, y))  # Add to variable

        elif 'plot' in request.POST:  # Plot button was clicked
            plot_url = self.plot_all()

        context = {
            'is_checked':is_checked,
            'point_form': point_form,  # Form object for creating points
            'line_form':line_form,
            'plot_url': plot_url,  # URL for the img (null initially)
            'points': points,  # List of points created so far
            'lines':lines,
        }
        return render(request, 'plotter.html', context)

    def plot_all(self):
        global is_checked
        plt.figure(figsize=(6, 4))  # Canvas size in inches
        if points:
            for p in points:
                plt.scatter(p.x, p.y, color='blue')
            if is_checked:
                xs = [p.x for p in points]  # Get all x values
                ys = [p.y for p in points]  # Get all y values
                plt.plot(xs, ys, color='gray', linestyle='--')
        if lines:
            p1s=[]
            p2s=[]
            for l in lines:
                plt.scatter(l.p1.x, l.p1.y, color='blue')
                plt.scatter(l.p2.x, l.p2.y, color='blue')
                plt.plot([l.p1.x, l.p2.x], [l.p1.y, l.p2.y], color='black', linestyle='-')

        plt.xlabel("X")
        plt.ylabel("Y")

        buf = io.BytesIO()  # Create buffer
        plt.savefig(buf, format='png')  # Saving the image into buffer
        buf.seek(0)  # We go back to the beginning of the stream
        plot_url = base64.b64encode(buf.read()).decode('utf-8')
        # DATA FLOW:
        # binary data -> bytes object (base 64-ASCII) -> text
        buf.close()
        plt.close()
        return plot_url