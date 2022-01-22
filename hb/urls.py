
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home' ),
    path('gettemp/<str:pk>',views.gettemp,name='gettemp' ),
    path('getwtemp/<str:pk>',views.getwtemp,name='getwtemp' ),
    path('gethumid/<str:pk>',views.gethumid,name='gethumid' ),
    path('getwlevel/<str:pk>',views.getwlevel,name='getwlevel' ),
    path('settemp/<str:pk>/<str:temp>',views.setTemp,name='settemp'),
    path('setwtemp/<str:pk>/<str:temp_w>',views.setwTemp,name='setwtemp'),
    path('sethumid/<str:pk>/<str:humid>',views.sethumid,name='sethumid'),
    path('setwlevel/<str:pk>/<str:w_level>',views.setwlevel,name='setwlevel'),
    path('getpumpstat/<str:pk>',views.getpumpstat,name='getpumpstat' ),
    path('togglepump/<str:pk>',views.Togglepump,name='togglepump' ),
    path('applogin',views.AppLogin,name='applogin')
]
