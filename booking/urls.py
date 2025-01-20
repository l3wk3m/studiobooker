from django.urls import path
from . import views


urlpatterns = [
    path('', views.booker, name="bookings"),
#    path('bookings/', views.booker, name="bookings"),
    path('<int:studio_id>/', views.studio_detail, name='studio_detail'),
    path('<int:studio_id>/booking_submit/', views.booking_submit, name='booking_submit'),
    path('booking_success/', views.booking_success, name='booking_success'),
    path('user_panel/', views.user_panel, name='user_panel'),
    path('user_update/<uuid:booking_id>/', views.user_update, name='user_update'),
    path('user_update_submit/<uuid:booking_id>/', views.user_update_submit, name='user_update_submit'),
    path('update_success/', views.update_success, name='update_success'),
    path('staff_panel/', views.staff_panel, name='staff_panel'),
]