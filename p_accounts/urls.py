from django.urls import path
from .views import *

urlpatterns = [
    path('reg/', reg, name='reg'),
    path('', log_in, name='login'),
    path('log_out/', log_out, name='logout'),
]
