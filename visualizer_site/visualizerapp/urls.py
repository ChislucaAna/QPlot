from django.urls import path
from .views import index, plot,home,signup
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name='home'),
    path('plot/', plot, name='plotter'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html', next_page='/'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('signup/',signup,name='signup'),
]
