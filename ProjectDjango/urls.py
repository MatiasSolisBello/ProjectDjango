from django.contrib import admin
from usuario import views
from django.urls import path
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('usuario', views.usuario, name="usuario"),
    path('mascota', views.mascota, name="mascota"),
    path('usuario_agregar', views.usuario_agregar, name="usuario_agregar"),
    path('usuario_eliminar/<id>/', views.usuario_eliminar, name="usuario_eliminar"),
    path('usuario_actualizar/<id>/', views.usuario_actualizar, name="usuario_actualizar"),
    path('mascota_agregar', views.mascota_agregar, name="mascota_agregar"),
    path('mascota_eliminar/<id>/', views.mascota_eliminar, name="mascota_eliminar"),
    path('mascota_actualizar/<id>/', views.mascota_actualizar, name="mascota_actualizar"),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)
