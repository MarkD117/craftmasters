from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Category, Project
from .forms import CommentForm, AddProjectForm, UpdateProjectForm


class LandingPage(generic.ListView):
    model = Project
    # Retrieves latest 4 projects in database
    queryset = Project.objects.filter(status=1).order_by('-created_on')[:4]  
    template_name = 'index.html'


class CategoryPage(View):
    def get(self, request, cat_name, *args, **kwargs):
        # Getting Category object based on the category name
        category = get_object_or_404(Category, category_name=cat_name)
        # Filter projects based on category, excluding draft posts
        project_category = Project.objects.filter(
            category=category,
            status=1  # Exclude draft posts by filtering based on status
        )
        return render(request, 'categories.html', {'cat_name': cat_name, 'project_category': project_category})


class ProjectList(generic.ListView):
    model = Project
    # queryset contains projects that have been published in descending order
    queryset = Project.objects.filter(status=1).order_by('-created_on')
    template_name = 'projects.html'
    # if there are more than 6 projects, page navigation will be added
    paginate_by = 6


class ProjectDrafts(LoginRequiredMixin, generic.ListView):
    model = Project
    template_name = 'project_drafts.html'
    # defining variable name for template
    context_object_name = 'drafted_projects'
    paginate_by = 6

    def get_queryset(self):
        return Project.objects.filter(author=self.request.user, status=0).order_by('-created_on')


@login_required
def AddProject(request):
    if request.method == 'POST':
        # Creating form instance and pass current user to form
        form = AddProjectForm(request.POST, request.FILES, user=request.user)
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


@login_required
def UpdateProject(request, slug):
    # Retrieving project instance to edit
    project = get_object_or_404(Project, slug=slug)

    # Checks if logged-in user is author or a superuser
    if request.user == project.author or request.user.is_superuser:
        if request.method == 'POST':
            # Getting updated form
            form = UpdateProjectForm(request.POST, request.FILES, instance=project)
            if form.is_valid():
                form.save()
                # Redirects to updated project page
                return redirect('project_detail', slug=project.slug)
        else:
            # Populating form fields with current values
            form = UpdateProjectForm(instance=project)

        # Passing updated form/project data to template
        context = {'update_project_form': form, 'project': project}
        return render(request, 'update_project.html', context)
    else:
        # If  user is not author or superuser, raise a 404 error
        raise Http404("You don't have permission to edit this project.")


@login_required
def DeleteProject(request, slug):
    # Retrieving project instance to delete
    project = get_object_or_404(Project, slug=slug)
    
    # Checks if logged-in user is author or a superuser
    if request.user == project.author or request.user.is_superuser:
        if request.method == 'POST':
            project.delete()
            return redirect('projects')
        else:
            # Redirects to detail page if method is not 'POST'
            return render(request, 'project_detail.html', {'project': project})
    else:
        # Raises a 404 error if user is not the author or is a super user
        raise Http404("You don't have permission to delete this project.")


class ProjectDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Project.objects.all()
        if not request.user.is_authenticated:
            # Only shows published posts to non-logged-in users
            queryset = queryset.filter(status=1)

        # Gets a published project with the correct slug
        project = get_object_or_404(queryset, slug=slug)

        if request.user == project.author or request.user.is_superuser:
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
        elif project.status == 0:
            raise Http404("You don't have permission to view this project.")
        else:
            comments = project.comments.filter(approved=True).order_by('created_on')
            liked = False
            if project.likes.filter(id=self.request.user.id).exists():
                liked = True

            return render(
                request,
                'project_detail.html',
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