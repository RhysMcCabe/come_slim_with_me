from django.urls import path
from .views import(    
    CategoryListView,
    CategoryCreateView,
    CategoryDeleteView,
    CategoryDetailView,
    TodoListView,
    TodoCreateView,
    TodoDeleteView,
    TodoDetailView,
    TodoUpdateView,
)

urlpatterns = [
     path('todo/<int:pk>/edit/', TodoUpdateView.as_view(), name='todo_edit'),
     path('todo/<int:pk>/delete/', TodoDeleteView.as_view(), name='todo_delete'),
     path('new_todo/', TodoCreateView.as_view(), name='todo_new'),
     path('todos', TodoListView.as_view(), name='todo_list'),
     path('todo/<int:pk>', TodoDetailView.as_view(), name='todo_detail'),
     path('category', CategoryListView.as_view(), name='category'),
     path('category/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category_delete'),
     path('category/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
     path('category_new/', CategoryCreateView.as_view(), name='category_new'),
]