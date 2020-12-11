from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Category, Todo
from braces.views import SelectRelatedMixin
from datetime import datetime
from django.db.models import Q





class CategoryListView(ListView):
    model = Category
    template_name = 'todo_base.html'
    context_object_name = 'all_categories_list'

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category_detail.html'

class CategoryCreateView(CreateView):
    model = Category
    template_name = 'category_new.html'
    fields = ('name',)
    success_url = reverse_lazy('category')

    def form_valid(self, form):
        form.instance.member = self.request.user
        return super().form_valid(form)

class CategoryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Category
    template_name = 'category_delete.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        obj = self.get_object()
        return obj.member == self.request.user

class TodoListView(ListView):
    model = Todo
    template_name = 'todo_list.html'
    context_object_name = 'todo_list'
    select_related = ("member", "category")
    date_created = ("dates")
    paginate_by = 5

class TodoDetailView(DetailView):
    model = Todo
    template_name = 'todo_detail.html'
    select_related = ("member", "category")

class TodoUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Todo
    fields = ('title', 'description', 'completed',)
    template_name = 'todo_edit.html'
    success_url = reverse_lazy('todo_list')

    def test_func(self):
        obj = self.get_object()
        return obj.member == self.request.user


class TodoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Todo
    template_name = 'todo_delete.html'
    success_url = reverse_lazy('todo_list')

    def test_func(self):
        obj = self.get_object()
        return obj.member == self.request.user


class TodoCreateView(CreateView):
    model = Todo
    template_name = 'todo_new.html'
    fields = ('title', 'description', 'completed', 'category',)
    success_url = reverse_lazy('todo_list')

    def form_valid(self, form):
        form.instance.member = self.request.user
        return super().form_valid(form)

    def get_form(self, *args, **kwargs):
        form = super(TodoCreateView, self).get_form(*args, **kwargs)
        form.fields['category'].queryset = Category.objects.filter(member=self.request.user) 
        return form
