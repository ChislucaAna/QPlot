from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render,redirect
#for login and signup ux i used predefined 
# models,forms, and functions

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