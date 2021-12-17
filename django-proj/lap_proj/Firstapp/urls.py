from . import views
from django.urls import path


urlpatterns = [
    path('laptop/',views.laptopview,name='lap'),
    path('show/',views.showlaptop,name='show_sh'),
    path('delete/<int:id>/',views.deleteview,name='del'),
    path('update/<int:id>/',views.updateview,name='upd'),


]