from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from graphene_django.views import GraphQLView
from .graphql.schema import schema

catchall = TemplateView.as_view(template_name='index.html')

urlpatterns = [
    path('', catchall),
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns += [path("graphql/", GraphQLView.as_view(graphiql=True, schema=schema))] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += [path("graphql/", GraphQLView.as_view(schema=schema))]
