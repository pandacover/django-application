from django.urls import path
from . import views

urlpatterns = [
   path('staff', views.staff, name = 'staff'),
   path('support', views.support, name = 'support')
]