from django.urls import path
from .views import DiscussionListView, DiscussionDetailView

urlpatterns = [
    path('', DiscussionListView.as_view(), name='home'),
    path('discussion/<int:pk>/', DiscussionDetailView.as_view(),
         name='discussion_detail'),
]
