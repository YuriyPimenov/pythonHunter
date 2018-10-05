"""firstproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
#Для медиа файлов
from django.conf.urls.static import static
from django.conf import settings
# from testurlmap import views
#from teststaticapp import views
# from firstapp import views
from authapp import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('authapp/', views.authapp_home, name='authapp-home'),
    path('authapp/login/', auth_views.login,{'template_name':'authapp/login.html'}, name='authapp-login'),
    path('authapp/logout/', auth_views.logout,{'next_page':'/'}, name='authapp-logout'),
    
    # re_path(r'^(?P<pizza_id>\d+)/$', views.pizza_detail, name='pizza_detail'),
    # path('formpage', views.form_page, name='form-page'),
    # path('', views.index, name='index'),
    # path('test_app/', include('testurlmap.test_url'))
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
