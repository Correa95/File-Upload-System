from django.contrib import admin
from django.urls import path
from files import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/auth/register/", views.register, name="register")
    path("api/auth/login/", TokenObtainPairView.as_view(), name="token_obtain-pair"),
    path("api/auth/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/files/", views.files, name="files"),
    path("api/files/<int:file_id>/", views.file, name="file"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



urlpatterns = format_suffix_patterns(urlpatterns)




