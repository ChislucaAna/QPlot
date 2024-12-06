from django.urls import path
from django.contrib.auth import views as auth_views
from .views.homepage import home
from .views.dashboard import dashboard
from .views.signup import signup
from .views.plotter import PlotView
from .views.delete import *
from .views.info import line_info

urlpatterns = [
    path('', home, name='home'),
    path('plot/', PlotView.as_view(), name='plotter'), #atunci cand creezi proiect nou
    path('accounts/login/', auth_views.LoginView.as_view(next_page='/',template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('signup/',signup,name='signup'),
    path('dashboard/',dashboard,name='dashboard'),
    path('delete-line/<int:line_id>/', delete_line, name='delete_line'),
    path('delete-point/<int:point_id>/', delete_point, name='delete_point'),
    path('delete-function/<int:function_id>/', delete_function, name='delete_function'),
    path('delete-project/<int:project_id>/', delete_project, name='delete_project'),
    path('line_info/<int:line_id>/', line_info, name='line_info'),
    path('plotter/<int:id>/', PlotView.as_view(), name='plotter_with_id'), #atunci cand accesezi din projects vrei sa ai context
]
