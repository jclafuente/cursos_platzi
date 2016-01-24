"""Course views."""

from .models import (
    Course,
    Category,
)

from django.views.generic import ListView


class CoursesListView(ListView):

    model = Course


class CoursesListCategoriesView(ListView):

    model = Category
