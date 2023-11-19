from . import views
from django.urls import path


urlpatterns = [
    path('', views.LandingPage.as_view(), name='home'),
    path('projects/', views.ProjectList.as_view(), name='projects'),
    # Django path converters
    # 'slug' keyword name matches 'slug' parameter in get 
    # method of ProjectDetail class in blog/views.py file.
    path('projects/<slug:slug>/', views.ProjectDetail.as_view(), name='project_detail'),
    path('like/<slug:slug>/', views.ProjectLike.as_view(), name='project_like'),
    path('category/<str:cat_name>/', views.CategoryPage.as_view(), name='category'),
    path('add-project/', views.AddProject, name='add_project'),
    path('projects/<slug:slug>/edit/', views.UpdateProject, name='update_project'),
    path('projects/<slug:slug>/delete/', views.DeleteProject, name='delete_project'),
]
