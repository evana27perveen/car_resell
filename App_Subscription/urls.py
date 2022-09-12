from django.urls import path
from App_Subscription import views

app_name = 'App_Subscription'


urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('payment/', views.payment, name='payment'),
    path('purchased/', views.purchased_, name='purchased'),
    path('payment-completed/', views.completed_payment, name='payment-completed'),
]

