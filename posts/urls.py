"""Posts URLs"""
#Django
from django.urls import path

#Views
from posts import views 

urlpatterns = [
    path(
        route = '',
        view = views.PostFeedView.as_view(),
        name = 'feed'
    )
]