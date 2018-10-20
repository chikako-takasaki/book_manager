from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import ( LoginView, LogoutView )

from .models import Book
from .forms import ( BookForm, LoginForm )


class TopView(generic.TemplateView):
  template_name = 'register/top.html'

class LoginView(LoginView):
  form_class = LoginForm
  template_name = 'register/login.html'

class LogoutView(LoginRequiredMixin, LogoutView):
  template_name = 'register/top.html'


class BookIndexView(generic.ListView):
  template_name = 'book_manager/index.html'
  context_object_name = 'latest_book_list'

  def get_queryset(self):
    """
    Return the last five published questions (not including those set to be
    published in the future).
    """
    return Book.objects.filter(
      created_at__lte=timezone.now()
    ).order_by('-created_at')[:5]

class BookListView(LoginRequiredMixin, generic.ListView):
  template_name = 'book_manager/book_list.html'
  context_object_name = 'latest_book_list'

  def get_queryset(self):
    """
    Return the last five published questions (not including those set to be
    published in the future).
    """
    return Book.objects.filter(
      created_at__lte=timezone.now()
    ).order_by('-created_at')[:5]

class BookRegisterView(LoginRequiredMixin, generic.ListView):
  template_name = 'book_manager/book_register.html'

  def get_queryset(self):
    """
    Return the last five published questions (not including those set to be
    published in the future).
    """
    return Book.objects.filter(
      created_at__lte=timezone.now()
    ).order_by('-created_at')[:5]

class BookSearchView(LoginRequired_Mixin, generic.ListView):
  template_name = 'book_manager/book_search.html'


class DetailView(LoginRequiredMixin, generic.DetailView):
  model = Book
  template_name = 'book_manager/detail.html'

  def get_queryset(self):
    """
    Excludes any questions that aren't published yet.
    """
    return Book.objects.filter(created_at__lte=timezone.now())

@login_required
def book_register(request):
  form = BookForm(request.POST or None)
  if form.is_valid():
    book = Book.objects.create(status = 1, **form.cleaned_data)
    return HttpResponseRedirect(reverse('book_manager:detail', args=(book.id,)))
  context = {
        'form': form,
  }
  return render(request, 'book_manager/book_register.html', context)

@login_required
def borrow(request, book_id):
  book = get_object_or_404(Book, pk=book_id)
  book.borrow_book()
  return HttpResponseRedirect(reverse('book_manager:detail', args=(book.id,)))

@login_required
def return_book(request, book_id):
  book = get_object_or_404(Book, pk=book_id)
  book.return_book()
  return HttpResponseRedirect(reverse('book_manager:detail', args=(book.id,)))
