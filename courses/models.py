from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=50)
    badge = models.ImageField(upload_to='media/courses/categories')

    def get_badge(self):
        return """<img src="{}" width="60" />""".format(
            self.badge.url)
    get_badge.allow_tags = True

    def __str__(self):
        return self.name


class Career(models.Model):

    name = models.CharField(max_length=60)
    badge = models.ImageField(upload_to='media/courses/careers')

    def get_badge(self):
        return """<img src="{}" width="60" />""".format(
            self.badge.url)
    get_badge.allow_tags = True

    def __str__(self):
        return self.name


class Instructor(models.Model):

    name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='media/courses/instructors')
    job_title = models.CharField(max_length=60)
    company = models.CharField(max_length=60)
    twitter_handle = models.CharField(max_length=30)

    def get_picture(self):
        return """<img src="{}" width="60" />""".format(
            self.picture.url)
    get_picture.allow_tags = True

    def __str__(self):
        return "{} - {} at {}".format(
            self.name,
            self.job_title,
            self.company
        )


class Course(models.Model):

    name = models.CharField(max_length=140)
    slug = models.SlugField(max_length=140, unique=True)
    description = models.TextField(max_length=800, blank=True)
    badge = models.ImageField(upload_to='media/courses/badges')
    youtube_video = models.URLField(max_length=400, blank=True)

    category = models.ForeignKey(Category)
    careers = models.ManyToManyField(Career)
    instructors = models.ManyToManyField(Instructor)

    def get_badge(self):
        return """<img src="{}" width="60" />""".format(
            self.badge.url)
    get_badge.allow_tags = True

    def __str__(self):
        return self.name


class Skill(models.Model):

    course = models.ForeignKey(Course)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/courses/skills')

    def get_image(self):
        return """<img src="{}" width="60" />""".format(
            self.image.url)
    get_image.allow_tags = True

    def __str__(self):
        return "{} - {}".format(self.course.name, self.title)


class SyllabusTopic(models.Model):

    course = models.ForeignKey(Course)
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.course.name
