from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title='Stepic DRF tests API',
        default_version='v1',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

api_patterns = [
    path('books/', include(('src.apps.books.urls', 'books'), namespace='books')),

    path('docs/', schema_view.with_ui('swagger', cache_timeout=0)),  # noqa
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls')),
    path('api/v1/', include(api_patterns)),
]
