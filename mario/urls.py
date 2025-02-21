from django.contrib import admin
from django.urls import path
from files import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name="home"),
    path("files/", views.files, name="files"),
    path("file/<int:file_id>/", views.file, name="file")

]
