from django.conf.urls import url

from .views import (
    CoursesListView,
)

urlpatterns = [

    url(r'^$', CoursesListView.as_view(), name='list'),

]