from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("index.urls")),
    path("next/", include("zakazy.urls")),
    path("user/", include("users.urls")),
    path("op/", include("ocenki.urls")),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
