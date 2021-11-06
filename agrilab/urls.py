from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("hotbox/", include("hotbox.urls")),
    path("admin/", admin.site.urls),
]
