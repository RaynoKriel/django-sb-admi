from django.urls import path, re_path
from apps.projects import views
# from app.projects.views import (
#                            projects_create_view,
#                            projects_delete_view,
#                            projects_list_view,
#                            dynamic_lookup_view,
#                            projects_update_view)


urlpatterns = [
    path('', views.projects_list_view, name='project-list'),
    path('create/', views.projects_create_view, name='project-create'),
    path('<int:id>/', views.dynamic_lookup_view, name='project-detail'),
    path('<int:id>/update/', views.projects_update_view, name='project-update'),
    path('<int:id>/delete/', views.projects_delete_view, name='project-delete'),
]
