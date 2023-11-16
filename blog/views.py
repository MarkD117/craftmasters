from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Category, Project
from .forms import CommentForm


class LandingPage(generic.ListView):
    model = Project
    # Retrieves latest 4 projects in database
    queryset = Project.objects.filter(status=1).order_by('-created_on')[:4]  
    template_name = 'index.html'

    # overriding 'get_context_data' method
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # adding categories to context for access in template
        context['categories'] = Category.objects.all()
        return context


class ProjectList(generic.ListView):
    model = Project
    # queryset contains projects that have been published in descending order
    queryset = Project.objects.filter(status=1).order_by('-created_on')
    template_name = 'projects.html'
    # if there are more than 6 projects, page navigation will be added
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


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
        
        # Gets categories to access in template
        categories = Category.objects.all()

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
                'categories': categories,
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