
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(pattern_name='inicio', permanent=False)),
    path('diagnostico/', include('diagnostico.urls')),
    path('recursos/', include('recursos.urls')),
    path('usuarios/', include('usuarios.urls')),

]
