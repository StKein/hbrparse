from django.urls import include, path
from .views import PostViewSet

urlpatterns = [
    path('', PostViewSet.list),
    path('<int:pk>/', PostViewSet.retrieve)
]