from django.shortcuts import render, redirect
from django.views import View
import matplotlib
matplotlib.use('Agg')  # Fixing: UserWarning: Starting a Matplotlib GUI outside of the main thread will likely fail.
import matplotlib.pyplot as plt  # Modulul pt plotting
import io
import base64

# Forms for creating new geometric plots:
from visualizerapp.forms import PointForm, TriangleForm  # Assuming TriangleForm is defined in forms.py

# Storage variables for geometric elements 
points = []
plot_url=None

class PlotView(View):
    def get(self, request, *args, **kwargs):
        global plot_url
        form = PointForm()  # Creating new instance of PointForm
        triangle_form = TriangleForm()  # Creating new instance of TriangleForm
        context = {
            'form': form,  # Form object for creating points
            'triangle_form': triangle_form,  # Form object for creating triangles
            'plot_url': plot_url,  # URL for the img (null initially)
            'points': points,  # List of points created so far
        }
        return render(request, 'plotter.html', context)

    def post(self, request, *args, **kwargs):
        global plot_url
        global points  # Referencing the global var
        form=PointForm()

        if 'add_point' in request.POST:  # Add point button was clicked
            form = PointForm(request.POST)
            if form.is_valid():
                # Django forms validate data automatically and it is added to cleaned_data
                x = form.cleaned_data['x']
                y = form.cleaned_data['y']
                points.append((x, y))  # Add to variable
                #return redirect('plotter')  # Redirect to the same view to show updated points

        elif 'plot' in request.POST:  # Plot button was clicked
            plot_url = self.plot_points()  # Call to plot points

        context = {
            'form': form,  # Form object for creating points
            'plot_url': plot_url,  # URL for the img (could be set now)
            'points': points,  # List of points created so far
        }
        return render(request, 'plotter.html', context)

    def plot_points(self):
        plt.figure(figsize=(6, 4))  # Canvas size in inches
        if points:
            xs, ys = zip(*points)  # Separate x and y values
            # Plotting points
            plt.scatter(xs, ys, color='blue')
            # Uncomment to connect points:
            # plt.plot(xs, ys, color='gray', linestyle='--')
        plt.title("Plot of Points")
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