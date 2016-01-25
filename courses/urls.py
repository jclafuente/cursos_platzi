from django.conf.urls import url

from .views import (
    CourseDetailView,
    CoursesListCareersView,
    CoursesListCategoriesView,
    CoursesListView,
)

urlpatterns = [

    url(
        r'^$',
        CoursesListView.as_view(),
        name='list'
    ),

    url(
        r'^categorias$',
        CoursesListCategoriesView.as_view(),
        name='list_categories'
    ),

    url(
        r'^carreras$',
        CoursesListCareersView.as_view(),
        name='list_careers'
    ),

    url(
        r'^(?P<slug>[^/]+)/$',
        CourseDetailView.as_view(),
        name='detail'
    ),

]