from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("testing_frontend/", include("frontend_views_and_designs.urls"))
]
