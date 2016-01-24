from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from django.views.generic.base import RedirectView

from platzi.settings import base as settings

from courses import urls as courses_urls

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='/cursos')),
    url(r'^cursos/', include(courses_urls, namespace='courses')),
    url(r'^platzi-admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # NOQA