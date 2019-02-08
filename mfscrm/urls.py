from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path, re_path
from django.contrib.auth.views import LoginView, LogoutView
# from . import views


urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include('crm.urls')),
    re_path(r'^accounts/login/$', LoginView.as_view(template_name='registration/login.html'), name="login"),
    # re_path(r'^accounts/profile/$', views.home, name='home'),
    re_path(r'^accounts/logout/$', LogoutView.as_view(), LogoutView.next_page, name="logout"),
    path('accounts/', include('django.contrib.auth.urls')),

    # path('', views.home, name='home'),
    # re_path(r'^home/$', views.home, name='home'),

]