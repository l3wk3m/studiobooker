from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="home"),
    path('bookings/', views.booker, name="bookings"),
    path('blog/', views.booker, name="blog"),
]