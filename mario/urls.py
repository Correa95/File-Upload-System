from django.contrib import admin
from django.urls import path
from files import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.home, name='home'),
    path('api/file/', views.getFile, name='file'),
    path("files/", views.files, name="files"),
]
urlpatterns = format_suffix_patterns(urlpatterns)

#     path("file/<int:file_id>/", views.file, name="file"),
#     path('files/edit/<int:file_id>/', views.edit, name='edit'),
#     path('files/delete/<int:file_id>/', views.delete, name='delete'),

#     path('files/upload/', views.upload, name='upload')
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



