from . import views
from django.urls import path


urlpatterns = [
    path('', views.LandingPage.as_view(), name='home'),
    path('projects/', views.ProjectList.as_view(), name='projects')
]
