"""Course views."""

from .models import (
    Course,
)

from django.views.generic import ListView


class CoursesListView(ListView):

    model = Course
