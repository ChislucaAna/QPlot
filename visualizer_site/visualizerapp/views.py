from django.shortcuts import render,redirect
from django.http import HttpResponse
import matplotlib.pyplot as plt
import numpy as np
from django.contrib.auth.forms import UserCreationForm
import os
from django.contrib.auth import login
def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request,'home.html')

def plot(request):
    # Generate a simple plot
    plt.figure()
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    plt.plot(x, y, label='Sine Wave', color='blue')
    plt.title('Sine Wave Plot')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.legend()

    # Save the plot to a file
    plot_file = 'plot.png'
    plt.savefig(plot_file)
    plt.close()  # Close the figure to free memory

    with open(plot_file, 'rb') as f:
        return HttpResponse(f.read(), content_type='image/png')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save() 
            user = form.save()
            login(request, user) 
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})