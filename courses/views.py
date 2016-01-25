"""Course views."""

from .models import (
    Career,
    Category,
    Course,
)

from django.views.generic import ListView
from django.views.generic.detail import DetailView

class CoursesListView(ListView):

    model = Course


class CoursesListCategoriesView(ListView):

    model = Category


class CoursesListCareersView(ListView):

    model = Career


class CourseDetailView(DetailView):

    model = Course
