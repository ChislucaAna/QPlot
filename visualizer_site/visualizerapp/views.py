from django.shortcuts import render,redirect #for UX flow
import matplotlib
matplotlib.use('Agg') #fixing:
#UserWarning: Starting a Matplotlib GUI outside 
#of the main thread will likely fail.
import matplotlib.pyplot as plt #modulul pt plotting
#for login and signup ux i used predefined 
# models,forms, and functions
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
#io allows us to create a buffer to store the image
#without creating a file, that we then encode into a base64
#string, that we will include in the src attribute for img
import io
import base64
#forms for creating new geometric plots:
from .forms import PointForm

#storage variabes for geometric elements 
points = []


def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request,'home.html')

def dashboard(request):
    return render(request,'dashboard.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save() #saving user into db
            #user is being logged in automatically
            user = form.save()
            login(request, user) 
            return redirect('/')
    else: #for GET request method
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def plot_view(request):
    global points #refferencing the global var
    plot_url = None #new variable for storing fututre img url
    form = PointForm()#creating new instance of pointform

    if request.method == 'POST':
        if 'add_point' in request.POST:  # Add point button was clicked
            form = PointForm(request.POST)
            if form.is_valid():
                #django forms validate data automatically and it is added to cleaned_data
                x = form.cleaned_data['x']
                y = form.cleaned_data['y']
                points.append((x, y)) #add to variable
        elif 'plot' in request.POST:  # Plot button was clicked
            plt.figure(figsize=(6, 4)) #canvas size in inches
            if points:
                xs, ys = zip(*points)  # Separate x and y values
                #plottinf points
                plt.scatter(xs, ys, color='blue')
                #pentru a uni punctele:
                #plt.plot(xs, ys, color='gray', linestyle='--')
            plt.title("Plot of Points")
            plt.xlabel("X")
            plt.ylabel("Y")
            
            buf = io.BytesIO() #create buffer
            plt.savefig(buf, format='png')#saving the image into bugger
            buf.seek(0) #we go back to beggining of the stream
            plot_url = base64.b64encode(buf.read()).decode('utf-8')
            #DATA FLOW:
            #binarydata->byes object(base 64-ASCII)->text
            buf.close()
            plt.close()

    context = {
        'form': form,#form object for creating points
        'plot_url': plot_url, #url for the img(null initially)
        'points': points, #list of points created so far
    }
    return render(request, 'plotter.html', context)
