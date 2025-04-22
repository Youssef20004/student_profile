from django.urls import path
from .views import login_view, profile_view, export_students_to_excel, StudentDetailView

urlpatterns = [
    path('', login_view, name='login'),
    path('profile/', profile_view, name='profile'),
    path('export/', export_students_to_excel, name='export_students'),
    path('api/students/<str:identifier>/', StudentDetailView.as_view(), name='student-detail'),
]

