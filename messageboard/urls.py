from django.urls import path
from .views import DiscussionListView, DiscussionDetailView, TopicListView

urlpatterns = [
    path('discussion/', DiscussionListView.as_view(), name='discussion'),
    path('discussion/<int:pk>/', DiscussionDetailView.as_view(),
         name='discussion_detail'),
    path('', TopicListView.as_view(), name='topic'),
]
