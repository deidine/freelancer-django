from django.urls import path
from . import views

urlpatterns = [
    # page projects
    path('projects/', views.projects, name="projects"),
    path('post-project/', views.post_projects, name="post-project"),
    path('post-project/delete/<int:project_id>', views.delete_post_projects, name="delete-post-project"),
    path('projects/search/', views.search_projects, name="search-projects"),
    path('projects/filter/', views.filter_project, name="filter-projects"),
    path('projects/edit-post/<int:pk>/', views.edit_post_project, name="edit-post-project"),
   
    # page Jobs
    path('jobs/', views.jobs, name="jobs"),
    path('post-job/', views.post_job, name="post-job"),
    path('post-job/delete/<int:job_id>', views.delete_post_jobs, name="delete-post-job"),
    path('jobs/edit-post/<int:pk>/', views.edit_post_job, name="edit-post-job"),
    path('jobs/search/', views.search_jobs, name="search-jobs"),
    path('jobs/filter/', views.filter_jobs, name="filter-jobs"),
 


]