from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Category, Project
from .forms import CommentForm, AddProjectForm


class LandingPage(generic.ListView):
    model = Project
    # Retrieves latest 4 projects in database
    queryset = Project.objects.filter(status=1).order_by('-created_on')[:4]  
    template_name = 'index.html'


class CategoryPage(View):
    def get(self, request, cat_name, *args, **kwargs):
        # Getting Category object based on the category name
        category = get_object_or_404(Category, category_name=cat_name)
        # Filter projects based on category
        project_category = Project.objects.filter(category=category)
        return render(request, 'categories.html', {'cat_name': cat_name, 'project_category': project_category})


class ProjectList(generic.ListView):
    model = Project
    # queryset contains projects that have been published in descending order
    queryset = Project.objects.filter(status=1).order_by('-created_on')
    template_name = 'projects.html'
    # if there are more than 6 projects, page navigation will be added
    paginate_by = 6


@login_required
def AddProject(request):
    if request.method == 'POST':
        # Creating form instance and pass current user to form
        form = AddProjectForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            # Redirects to the project detail page for new project
            # Passes slug of instance as parameter
            return redirect('project_detail', slug=form.instance.slug)
    else:
        # If form is not being submitted, current user is passed to form
        form = AddProjectForm(user=request.user)

    # Form passed as context to template
    context = {'add_project_form': form}
    return render(request, 'add_project.html', context)


class ProjectDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Project.objects.filter(status=1)
        # Gets a published project with the correct slug
        project = get_object_or_404(queryset, slug=slug)
        # Gets comments of the project ordered by oldest 1st
        comments = project.comments.filter(approved=True).order_by('created_on')
        liked = False
        # If the user id exists to say a user has liked
        # the project, the liked value will be set to True
        if project.likes.filter(id=self.request.user.id).exists():
            liked = True

        # Sending all information to the render method
        return render(
            # Sending request
            request,
            # Specifying the template required
            'project_detail.html',
            # Using a dictionary to supply context
            {
                'project': project,
                'comments': comments,
                'commented': False,
                'liked': liked,
                'comment_form': CommentForm(),
            },
        )
    
    def post(self, request, slug, *args, **kwargs):
        queryset = Project.objects.filter(status=1)
        project = get_object_or_404(queryset, slug=slug)
        comments = project.comments.filter(approved=True).order_by('created_on')
        liked = False
        if project.likes.filter(id=self.request.user.id).exists():
            liked = True

        # Gets all of the data from the comment form
        comment_form = CommentForm(data=request.POST)

        # is.valid() checks if information 
        # has been submitted to the form.
        if comment_form.is_valid():
            # sets email and username automatically
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            # saves comment but does not commit 
            # until a post is assigned to it.
            comment = comment_form.save(commit=False)
            comment.project = project
            comment.save()
        else:
            # if the comment form is not valid, an
            # empty comment form instance is returned.
            comment_form = CommentForm()

        return render(
            request,
            'project_detail.html',
            {
                'project': project,
                'comments': comments,
                'commented': True,
                'liked': liked,
                'comment_form': CommentForm()
            },
        )

class ProjectLike(View):
    
    def post(self, request, slug):
        project = get_object_or_404(Project, slug=slug)

        # checking to see if the project has already been liked
        if project.likes.filter(id=request.user.id).exists():
            # Removes like
            project.likes.remove(request.user)
        else:
            # add like if it does not exists
            project.likes.add(request.user)

        # liking or unliking a project will reload the project_detail page and update the like
        return HttpResponseRedirect(reverse('project_detail', args=[slug]))