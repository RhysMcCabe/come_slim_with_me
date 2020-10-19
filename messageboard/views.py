from django.views.generic import ListView, DetailView
from .models import Discussion


class DiscussionListView(ListView):
    model = Discussion
    template_name = 'home.html'
    context_object_name = 'all_discussions_list'


class DiscussionDetailView(DetailView):
    model = Discussion
    template_name = 'discussion_detail.html'
