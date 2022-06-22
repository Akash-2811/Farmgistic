from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('webpages.urls')),
    path('authentication/', include('authentication.urls')),
    path('farmers/', include('farmers.urls')),
    path('traders/', include('traders.urls')),
    path('accounts/', include('allauth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
