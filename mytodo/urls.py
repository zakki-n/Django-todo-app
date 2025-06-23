from django.urls import path
from mytodo import views as mytodo

urlpatterns = [
    path("", mytodo.index, name="index"),
    path("add/", mytodo.add, name="add"),
    path("edit/<int:task_id>/", mytodo.edit_task, name="edit_task"),
    path("delete/<int:task_id>/", mytodo.delete_task, name="delete_task"),
    path("update_task_complete/", mytodo.update_task_complete, name="update_task_complete"),
]
