from django.contrib import admin
from usuario import views
from django.urls import path
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('/usuario', views.usuario, name="usuario"),
    path('/mascota', views.mascota, name="mascota"),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)
