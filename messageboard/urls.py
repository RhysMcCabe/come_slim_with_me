from django.urls import path
from .views import(
    DiscussionListView,
    DiscussionUpdateView,
    DiscussionDetailView,
    DiscussionDeleteView,
    DiscussionCreateView,
    TopicListView,
    CommentCreateView,
    TopicCreateView,
    SearchResultsListView,
    TopicsDetailView
)

urlpatterns = [

     path('topics/<int:pk>/', TopicsDetailView.as_view(), name='topics_detail'),
    path('topic_new/', TopicCreateView.as_view(), name='topic_new'),
    path('discussion/<int:discussion_pk>/comment/',
         CommentCreateView.as_view(), name='discussion_comment'),
    path('discussion/<int:pk>/edit/',
         DiscussionUpdateView.as_view(), name='discussion_edit'),
    path('discussion/<int:pk>/delete/',
         DiscussionDeleteView.as_view(), name='discussion_delete'),
    path('new/', DiscussionCreateView.as_view(), name='discussion_new'),
    path('discussions', DiscussionListView.as_view(), name='discussion_list'),
    path('discussion/<int:pk>/',
         DiscussionDetailView.as_view(), name='discussion_detail'),
    path('', TopicListView.as_view(), name='topic'),
    path('search/', SearchResultsListView.as_view(), name='search_results'),
]
