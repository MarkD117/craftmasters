from .models import Comment, Project, Category
from django import forms
from django.utils.text import slugify
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class CommentForm(forms.ModelForm):
    class Meta:
        # Setting Model used and field displayed
        model = Comment
        # trailing comma is neccessary for python 
        # to interpret as a tuple not a string
        fields = ('body',)


class AddProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['slug', 'author', 'project_images', 'likes']
        widgets = {
            'content': SummernoteWidget(),
        }

    def __init__(self, *args, **kwargs):
        # Getting the user interacting with form
        self.user = kwargs.pop('user', None)
        # Ensuring form is initialised properly
        super(AddProjectForm, self).__init__(*args, **kwargs)

        # Set custom label for title_image
        self.fields['title_image'].label = 'Title Image'

        # Exclude 'uncategorized' category from the queryset
        uncategorized_category = Category.objects.get(category_name='uncategorized')
        self.fields['category'].queryset = Category.objects.exclude(id=uncategorized_category.id)

    # Overriding save method to include customisations
    def save(self, commit=True):
        project = super().save(commit=False)
        project.author = self.user
        # Automatically generating slug
        project.slug = slugify(self.cleaned_data['title'])
        if commit:
            project.save()
        return project


class UpdateProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'title_image', 'category', 'description', 'content', 'status']
        widgets = {
            'content': SummernoteWidget(),
        }

    # Excluding 'uncategorized' category from update form
    def __init__(self, *args, **kwargs):
        super(UpdateProjectForm, self).__init__(*args, **kwargs)
        self.fields['title_image'].label = 'Title Image'
        uncategorized_category = Category.objects.get(category_name='uncategorized')
        self.fields['category'].queryset = Category.objects.exclude(id=uncategorized_category.id)
        
