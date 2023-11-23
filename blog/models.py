from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Category(models.Model):
    category_name = models.CharField(max_length=25)

    class Meta:
        # Correcting plural name in admin panel
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category_name


STATUS = ((0, 'Draft'), (1, 'Published'))


# Getting 'uncategorized' category id for default value.
# 'uncategorized' category must be created in admin panel
uncategorized_category = Category.objects.get(category_name='uncategorized')
uncategorized_category_id = uncategorized_category.id


class Project(models.Model):
    title = models.CharField(max_length=200, unique=True)
    title_image = CloudinaryField('image', default='placeholder')
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='project_posts'
        )
    # Gets categories from category model. Sets default value if
    # assigned category gets deleted
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_DEFAULT,
        default=uncategorized_category_id,
        null=True,
        related_name='project_categories'
    )
    description = models.TextField(blank=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='project_like', blank=True)

    class Meta:
        # order our posts with the created_on field in
        # descending order. newest posts listed 1st
        ordering = ['-created_on']

    # returns string representation of an object
    def __str__(self):
        return f"{self.title} by {self.author}"

    # returns the total number of likes on a post
    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE,
                                related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)

    class Meta:
        # order comments with the created_on field in
        # ascending order. Oldest comments listed 1st
        ordering = ['created_on']

    def __str__(self):
        return f'Comment {self.body} by {self.name}'
