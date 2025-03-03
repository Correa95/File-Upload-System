from django.contrib import admin
from django.urls import path
from files import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views.home, name='home'),
#     path('files/', views.files, name='files'),
#     path('file/<int:file_id>/', views.file, name='file'),
#     path('files/edit/<int:file_id>/', views.edit, name='edit'),
#     path('files/delete/<int:file_id>/', views.delete, name='delete'),
#     path('files/upload/', views.upload, name='upload')
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name="home"),
    path("api/files/", views.files, name="files"),
    path("api/files/<int:file_id>/", views.file, name="file"),
    path('api/file/', views.file, name='file'),
    path("api/auth/login/", TokenObtainPairView.as_view(), name="token_obtain-pair"),
    path("api/auth/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/auth/register/", views.register, name="register"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



urlpatterns = format_suffix_patterns(urlpatterns)




