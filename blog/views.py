from django.shortcuts import render
from django.views import generic, View
from .models import Category

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