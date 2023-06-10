from django.urls import path
from .views import *

urlpatterns = [
    path('index/', index, name='index'),

    path('profile/', profile, name='profile'),
    path('personal_info/', personal_info, name='personal_info'),

    path('all_iteams/', all_iteams, name='all_iteams'),

    path('persoprofdel/<int:id>/', persoprofdel, name='persoprod'),
    path('profdel/<int:id>/', profdel, name='profdelete'),

    path('update_p_profile/<int:id>/', update_p_profile, name='update_p_profile'),
    path('update_profile/<int:id>/', update_profile, name='update_profile'),
]
