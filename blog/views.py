from django.shortcuts import render
from django.views import generic, View
from .models import Category

class LandingPage(View):
    # Specifying the template name
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        context = {'categories': categories}
        return render(request, self.template_name, context)