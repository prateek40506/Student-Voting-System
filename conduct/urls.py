from django.urls import path
from . import views

urlpatterns = [
    path('<int:has_registered>/', views.voting, name='home'),
    path('<int:has_registered>/<str:first_name>/<str:last_name>/<str:voter_class>/<str:voter_section>/', views.voting, name='voting'),
    path('register', views.register, name='register'),
    path('contestant', views.contestant, name='contestant'),
    path('', views.login, name="login")
]
