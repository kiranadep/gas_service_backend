from django.urls import path
from . import views  # ✅ Correct import

urlpatterns = [
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create/', views.create_request, name='create_request'),
    path('view/<int:pk>/', views.view_request, name='view_request'),
]
