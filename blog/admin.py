from django.contrib import admin
from .models import Project, Comment, Category
# summernote library used to style project text
from django_summernote.admin import SummernoteModelAdmin


# register project model on admin portal
@admin.register(Project)
class ProjectAdmin(SummernoteModelAdmin):
    # adding filter funtionality to the admin portal
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on', 'category', 'author')
    # prepopulating the slug field based on the title
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'project', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    # Allows an admin to approve comments
    actions = ['approve_comments']

    # function allowing admin to set approved to True
    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name',)
