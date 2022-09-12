from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from Samia_and_Sami_Project.views import developerBase

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('App_login.urls')),
    path('', include('App_cars.urls')),
    path('Subscription/', include('App_Subscription.urls')),
    path('chat/', include('chat.urls')),
    path('Only-the-developer-can-access/', developerBase),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
