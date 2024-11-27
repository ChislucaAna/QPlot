from django.urls import path
from django.contrib.auth import views as auth_views
from .views.homepage import home
from .views.dashboard import dashboard
from .views.signup import signup
from .views.plotter import PlotView
from .views.delete import delete_line,delete_point
from .views.info import line_info

urlpatterns = [
    path('', home, name='home'),
    path('plot/', PlotView.as_view(), name='plotter'),
    path('login/', auth_views.LoginView.as_view(next_page='/',template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('signup/',signup,name='signup'),
    path('dashboard/',dashboard,name='dashboard'),
    path('delete-line/<int:line_id>/', delete_line, name='delete_line'),
    path('delete-point/<int:point_id>/', delete_point, name='delete_point'),
    path('line_info/<int:line_id>/', line_info, name='line_info'),
]
