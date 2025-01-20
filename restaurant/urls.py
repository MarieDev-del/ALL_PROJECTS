# from django.urls import path
# from . import views

# urlpatterns = [
#     path('book/', views.book, name='book'),
#     path('bookings/', views.bookings, name='bookings'),
# ]



# from django.urls import path
# from . import views

# urlpatterns = [
#     path('bookings/', views.booking_view, name='booking_form'),
#     path('api/bookings/', views.get_all_bookings, name='all_bookings'),
#     path('bookings/<str:date>/', views.get_bookings_for_date, name='bookings_for_date'),
#     path('booking_success/', views.booking_success, name='booking_success'),
# ]



from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('book/', views.book, name="book"),
    path('menu/', views.menu, name="menu"),
    path('menu_item/<int:pk>/', views.display_menu_item, name="menu_item"),  
    path('bookings/', views.bookings_list, name="bookings_list"),
    path('reservations/', views.bookings_api, name="bookings_api"),
    # path('reservations/', views.bookings_list, name="bookings_list"),
]






