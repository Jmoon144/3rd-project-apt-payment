from django.urls import path
from .views.public.views import PublicUserDetailView

urlpatterns = [
    path('/public/<int:pk>', PublicUserDetailView.as_view())
]
