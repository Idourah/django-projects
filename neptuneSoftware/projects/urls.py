from django.urls import path
from projects import views as project_view

urlpatterns = [
    path('home', project_view.ProjectListView.as_view(), name='dashboard'),
    path('create', project_view.CreateProjectFormView.as_view(), name="create-project"),
    path('<int:id>/update', project_view.UpdateProjectView.as_view(), name='update-project'),
    path('<int:id>/details', project_view.DetailProjectView.as_view(), name='detail-project'),
    path('<int:pk>/delete', project_view.DeleteProjectView, name='delete_project')
]
