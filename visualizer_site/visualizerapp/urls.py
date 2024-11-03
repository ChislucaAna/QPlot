from django.urls import path
from .views import index,home,signup,plot_view,dashboard
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name='home'),
    path('plot/', plot_view, name='plotter'),
    path('login/', auth_views.LoginView.as_view(next_page='/',template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('signup/',signup,name='signup'),
    path('dashboard/',dashboard,name='dashboard')
]
