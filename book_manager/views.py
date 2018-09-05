from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from .models import Book


class IndexView(generic.ListView):
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


