from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('profile/', include('profiles.urls')),
    path('accounts/', include('user.urls')),
    path('api/', include('api.urls')),
    path('wall/', include('wall.urls'))

]

handler404 = "main.views.page_not_found_view"

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)