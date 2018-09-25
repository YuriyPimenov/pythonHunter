from django.urls import path,re_path
from testurlmap import views

urlpatterns = [    
    # path('', views.home, name='home')
    # path('user/<int:month>/', views.home, name='home'),
    re_path(r'^user/(?P<month>[0-9]{2})/$', views.home, name='home'),
]