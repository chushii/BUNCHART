from datetime import datetime
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views, forms

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('links/', views.links, name='links'),
    path('pool/', views.pool, name='pool'),
    path('signup/', views.signup, name='signup'),
    path('login/',
         LoginView.as_view
         (
             template_name='main/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Логин',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
]

