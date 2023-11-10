from django.shortcuts import render
from django.views import generic, View


class LandingPage(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')
