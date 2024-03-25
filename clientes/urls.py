from django.urls import path
from .views import cliente_lista, clientes_new, clientes_update, clientes_delete
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('list/', cliente_lista, name = "clientes_list"),
    path('new/', clientes_new, name="clientes_new"),
    path('update/<int:id>/', clientes_update, name='clientes_update'), 
    path('delete/<int:id>/', clientes_delete, name='clientes_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # root de img