from django.urls import path
from .views import(
    DiscussionListView,
    DiscussionUpdateView,
    DiscussionDetailView,
    DiscussionDeleteView,
    DiscussionCreateView,
    TopicListView,
)

urlpatterns = [
    path('discussion/<int:pk>/edit/',
    DiscussionUpdateView.as_view(), name='discussion_edit'),
    path('discussion/<int:pk>/delete/',
    DiscussionDeleteView.as_view(), name='discussion_delete'),
    path('discussion/new/', DiscussionCreateView.as_view(), name='discussion_new'),
    path('topic/<int:pk>/', DiscussionListView.as_view(), name='discussion'),
    path('discussion/<int:pk>/', 
    DiscussionDetailView.as_view(), name='discussion_detail'),
    path('', TopicListView.as_view(), name='topic'),
]
