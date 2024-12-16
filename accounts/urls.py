from . import views
from accounts.views import*
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import *

urlpatterns=[
    #path('login/',views.login_view,name='login'),
    #path('fetch_service_provider_data/',views.fetch_service_provider_data,name='fetch_service_provider_data'),
    path('login/Librarian/', LoginView.as_view(), name='Librarian-login'),
    path('login/Superuser/', LoginView.as_view(), name='Superuser-login'),
    path('login/Office_staf/', LoginView.as_view(), name='Office_staff-login'),

]