from django.urls import path
from django.urls.resolvers import URLPattern
from .views import HomeView, SnackListView, SnackDetailView, SnackCreateView, SnackUpdateView, SnackDeleteView

urlpatterns = [
  path('', HomeView.as_view(), name='home'),
  path('snack_list/', SnackListView.as_view(), name='snack_list'),
  path('<int:pk>/', SnackDetailView.as_view(), name='snack_detail'),
  path('create/', SnackCreateView.as_view(), name='create_snack'),
  path('<int:pk>/update/', SnackUpdateView.as_view(), name='update_snack'),
  path('<int:pk>/delete/', SnackDeleteView.as_view(), name='delete_snack'),
]