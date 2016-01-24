from django.conf.urls import url

from .views import (
    CoursesListView,
    CoursesListCategoriesView,
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

]