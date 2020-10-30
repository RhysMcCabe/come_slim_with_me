from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Discussion, Topic, Comment
from braces.views import SelectRelatedMixin
from datetime import datetime
from django.db.models import Q

class DiscussionListView(ListView):
    model = Discussion
    template_name = 'discussion_list.html'
    context_object_name = 'all_discussions_list'
    select_related = ("member", "topic")
    date_created = ("dates")


class DiscussionDetailView(DetailView):
    model = Discussion
    template_name = 'discussion_detail.html'
    select_related = ("member", "topic")


class TopicListView(ListView):
    model = Topic
    template_name = 'home.html'
    context_object_name = 'all_topics_list'

class TopicsDetailView(DetailView):
    model = Topic
    template_name = 'topics_detail.html'


class DiscussionUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Discussion
    fields = ('title', 'body', 'image',)
    template_name = 'discussion_edit.html'

    def test_func(self):
        obj = self.get_object()
        return obj.member == self.request.user


class DiscussionDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Discussion
    template_name = 'discussion_delete.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        obj = self.get_object()
        return obj.member == self.request.user


class DiscussionCreateView(CreateView):
    model = Discussion
    template_name = 'discussion_new.html'
    fields = ('title', 'body', 'topic', 'image',)
    success_url = reverse_lazy('discussion_list')

    def form_valid(self, form):
        form.instance.member = self.request.user
        return super().form_valid(form)

class DiscussionSearchResultsView(ListView):
    model = Discussion
    context_object_name = 'all_discussions_list'
    template_name = 'discussion_search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('r')
        return Discussion.objects.filter(Q(title__icontains=query) | Q(body__icontains=query))

        


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'discussion_comment.html'
    fields = ('comment', 'image',)

    def form_valid(self, form):
        form.instance.member = self.request.user
        form.instance.discussion = Discussion.objects.get(
            pk=self.kwargs['discussion_pk'])
        return super().form_valid(form)


class TopicCreateView(CreateView):
    model = Topic
    template_name = 'topic_new.html'
    fields = ('name', 'description')
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.member = self.request.user
        return super().form_valid(form)

class TopicDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Topic
    template_name = 'topic_delete.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        obj = self.get_object()
        return obj.member == self.request.user

class TopicSearchResultsView(ListView):
    model = Topic
    context_object_name = 'all_topics_list'
    template_name = 'topic_search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Topic.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))


class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    fields = ('comment', 'image',)
    template_name = 'comment_edit.html'

    def test_func(self):
        obj = self.get_object()
        return obj.member == self.request.user
    


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'comment_delete.html'
    success_url = reverse_lazy('discussion_list')

    def test_func(self):
        obj = self.get_object()
        return obj.member == self.request.user