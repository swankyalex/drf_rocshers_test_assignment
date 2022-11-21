from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import path
from django.views.generic import RedirectView
from drf_spectacular.views import SpectacularAPIView
from drf_spectacular.views import SpectacularSwaggerView

urlpatterns = [
    path("", RedirectView.as_view(url="/api/v1")),
    path("admin/", admin.site.urls),
    # main application url
    path("api/v1/", include("api.urls")),
    # authorization and authentication urls
    path("api/users/", include("user.urls")),
    path("api-auth/", include("rest_framework.urls")),
    # spectacular doc urls
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
