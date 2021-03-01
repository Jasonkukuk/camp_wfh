from django.urls import path     
from . import views


######################################################################################
#                                Rendor Routes                                       *
######################################################################################

urlpatterns = [
    path('', views.index),
    path('dashboard', views.success),

######################################################################################
#                                 Action Routes                                      *
######################################################################################

    path('adduser', views.add_user),
    path('login', views.login), 	  
    path('logout', views.log_out), 
]