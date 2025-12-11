from django.urls import path
from .views import classes, class_by_id, class_sheet

urlpatterns = [
    path('', classes, name='classes'),
    path('<int:pk>/', class_by_id, name='class_by_id'),
    path('<int:pk>/sheet', class_sheet, name='class_sheet')
]