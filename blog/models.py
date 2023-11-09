from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, 'Draft'), (1, 'Published'))

class Project(models.Model):
    title = models.CharField(max_length=200, unique=True)
    title_image = CloudinaryField('image', default='placeholder')
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="project_posts"
        )
    category = models.CharField(max_length=25, default='uncategorized')
    description = models.TextField(blank=True)
    content = models.TextField()
    project_images = CloudinaryField('image', default='placeholder') 
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='project_like', blank=True)

    class Meta:
        # order our posts with the created_on field in 
        # descending order. newest posts listed 1st
        ordering = ["-created_on"]

    # returns string representation of an object
    def __str__(self):
        return f"{self.title} | {self.author}"

    # returns the total number of likes on a post
    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)

    class Meta:
        # order comments with the created_on field in 
        # ascending order. Oldest comments listed 1st
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"


class Category(models.Model):
    category_name = models.CharField(max_length=25)

    class Meta:
        # Correcting plural name in admin panel
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.name
