from django.urls import path
from .views import FishListCreateView, FishDetailView

urlpatterns = [
    path('', FishListCreateView.as_view(), name='fish-list-create'),
    path('fish/<int:pk>/', FishDetailView.as_view(), name='fish-detail'),
]
