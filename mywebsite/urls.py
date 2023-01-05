"""mywebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.contrib.auth import views as auth_views

#from django.views.generic.base import TemplateView,RedirectView

from database.views import predictImage

from .views import index, Login, Logout, Registration

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^database/', include('database.urls', namespace='database')),
    url(r'^predictImage$', predictImage, name='predictImage'),
    url(r'^password_reset/$', auth_views.PasswordResetView.as_view(), name='password_reset'),
    url(r'^password_reset/done/$', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[\w-]+)/(?P<token>[\w-]+)$', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    url(r'^Registration/', Registration, name='registration'),
    url(r'^Logout$', Logout, name='logout'),
    url(r'^Login$', Login, name='login'),
    url(r'^$', index, name='index'),

    

]
    #url(r'^prediction/$', views.prediction, name = 'prediction'), 
    #url(r'^home$', RedirectView.as_view(url='/'), name='home'),
    #url(r'^$', ParameterView.as_view(template_name = 'index.html')),
    
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA, document_root=settings.MEDIA_ROOT)