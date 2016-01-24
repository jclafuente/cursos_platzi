from django.conf.urls import url

from .views import (
    CoursesListView,
    CoursesListCategoriesView,
    CoursesListCareersView
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

]