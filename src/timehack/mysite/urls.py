from django.urls import path, include
from .api import api
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("api/", api.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
