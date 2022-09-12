from django.urls import path
from App_cars import views

app_name = 'App_cars'

urlpatterns = [
    path('', views.home, name="home"),
    path('service/', views.services, name="service"),
    path('car-store/', views.car_store, name="car-store"),
    path('car-search/', views.car_search, name="car-search"),
    path('blog/', views.blog_views, name="blog"),
    path('car-details/<int:pk>/', views.car_details, name='car-details'),
    path('blog-details/<int:pk>/', views.blog_details, name='blog-details'),
    path('reviews/', views.review, name='reviews'),
    path('checkviewFalse/', views.checkviewFalse, name='checkviewFalse')
]

