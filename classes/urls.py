from django.urls import path
from .views import classes, class_by_id

urlpatterns = [
    path('', classes, name="classes"),
    path('<int:pk>/', class_by_id, name="class_by_id")
]