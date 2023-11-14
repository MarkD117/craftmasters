from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Category, Project


class LandingPage(View):
    # Specifying the template name
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        # getting all categories
        categories = Category.objects.all()
        # passing categories as context to the template
        context = {'categories': categories}
        return render(request, self.template_name, context)


class ProjectList(generic.ListView):
    model = Project
    # queryset contains projects that have been published in descending order
    queryset = Project.objects.filter(status=1).order_by('-created_on')
    template_name = 'projects.html'
    # if there are more than 6 projects, page navigation will be added
    paginate_by = 6

    # overriding 'get_context_data' method
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # adding categories to context for access in template
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
                'categories': categories,
            },
        )