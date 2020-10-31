from django.urls import path
from .views import(
    DiscussionListView,
    DiscussionUpdateView,
    DiscussionDetailView,
    DiscussionDeleteView,
    DiscussionCreateView,
    DiscussionSearchResultsView,
    TopicListView,
    CommentCreateView,
    TopicCreateView,
    TopicSearchResultsView,
    TopicsDetailView,
    TopicDeleteView,
    CommentEditView,
    CommentDeleteView,
)

urlpatterns = [
     path('discussion/comment/<int:pk>/delete', CommentDeleteView.as_view(), name='comment_delete'),
     path('discussion/comment/<int:pk>/edit', CommentEditView.as_view(), name='comment_edit'),
     path('topics/<int:pk>/delete/', TopicDeleteView.as_view(), name='topic_delete'),
     path('topics/<int:pk>/', TopicsDetailView.as_view(), name='topics_detail'),
     path('topic_new/', TopicCreateView.as_view(), name='topic_new'),
     path('discussion/<int:discussion_pk>/comment/', CommentCreateView.as_view(), name='discussion_comment'),
     path('discussion/<int:pk>/edit/', DiscussionUpdateView.as_view(), name='discussion_edit'),
     path('discussion/<int:pk>/delete/', DiscussionDeleteView.as_view(), name='discussion_delete'),
     path('new/', DiscussionCreateView.as_view(), name='discussion_new'),
     path('discussions/search/',DiscussionSearchResultsView.as_view(), name='discussion_search_results'),
     path('discussions', DiscussionListView.as_view(), name='discussion_list'),
     path('discussion/<int:pk>/', DiscussionDetailView.as_view(), name='discussion_detail'),
     path('topics/search/', TopicSearchResultsView.as_view(), name='topic_search_results'),
     path('', TopicListView.as_view(), name='topic'),
    
]