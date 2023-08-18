
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from strawberry.django.views import GraphQLView
from api.schema import schema
urlpatterns = [
    path('admin/', admin.site.urls),
    path("graphql", GraphQLView.as_view(schema=schema))
]
    
# Media setting #
if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


