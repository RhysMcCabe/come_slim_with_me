from django.urls import path
from .views import(
    DiscussionListView,
    DiscussionUpdateView,
    DiscussionDetailView,
    DiscussionDeleteView,
    DiscussionCreateView,
    TopicListView,
    CommentCreateView,
    TopicCreateView
)

urlpatterns = [
    path('topic_new/', TopicCreateView.as_view(), name='topic_new'),
    path('discussion/<int:discussion_pk>/comment/',
         CommentCreateView.as_view(), name='discussion_comment'),
    path('discussion/<int:pk>/edit/',
         DiscussionUpdateView.as_view(), name='discussion_edit'),
    path('discussion/<int:pk>/delete/',
         DiscussionDeleteView.as_view(), name='discussion_delete'),
    path('new/', DiscussionCreateView.as_view(), name='discussion_new'),
    path('topic/<int:pk>/', DiscussionListView.as_view(), name='discussion_list'),
    path('discussion/<int:pk>/',
         DiscussionDetailView.as_view(), name='discussion_detail'),
    path('', TopicListView.as_view(), name='topic'),
]
