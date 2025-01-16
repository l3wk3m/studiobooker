from django.urls import path
from . import views


urlpatterns = [
    path('', views.booker, name="bookings"),
#    path('bookings/', views.booker, name="bookings"),
    path('<int:studio_id>/', views.studio_detail, name='studio_detail'),
    path('blog/', views.blog, name="blog"),
]