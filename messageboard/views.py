from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Discussion, Topic, Comment
from braces.views import SelectRelatedMixin


class DiscussionListView(ListView):
    model = Discussion
    template_name = 'discussion_list.html'
    context_object_name = 'all_discussions_list'
    select_related = ("member", "topic")


class DiscussionDetailView(DetailView):
    model = Discussion
    template_name = 'discussion_detail.html'
    select_related = ("member", "topic")


class TopicListView(ListView):
    model = Topic
    template_name = 'home.html'
    context_object_name = 'all_topics_list'

class DiscussionUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Discussion
    fields = ('title', 'body',)
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
    fields = ('title', 'body', 'topic')


    def form_valid(self, form):
        form.instance.member = self.request.user
        return super().form_valid(form)


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'discussion_comment.html'
    fields = ('comment',)

    def form_valid(self, form):
        form.instance.member = self.request.user
        form.instance.discussion = Discussion.objects.get(pk=self.kwargs['discussion_pk'])
        return super().form_valid(form)

class TopicCreateView(CreateView):
    model = Topic
    template_name = 'topic_new.html'
    fields = ('name', 'description')


    def form_valid(self, form):
        form.instance.member = self.request.user
        return super().form_valid(form)