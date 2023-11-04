from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler400, handler404, handler500
from app.views import custom_error_404, custom_error_500

handler404 = custom_error_404
handler500 = custom_error_500

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', include('app.urls', namespace='app')),
    path('api/v1/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', include('findstateAdmin.urls', namespace='admin')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
