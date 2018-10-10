from django.conf.urls import url, include
from . import views
from django.contrib import admin

app_name = 'book_manager'
urlpatterns = [
  # top page
  url(r'^$', views.TopView.as_view(), name='top'),
  
  # login, logout
  url(r'^login/$', views.LoginView.as_view(), name='login'),
  url(r'^logout/$', views.LogoutView.as_view(), name='logout'),

  url(r'^book_index/$', views.BookIndexView.as_view(), name='book_index'),
  url(r'^book_list/$', views.BookListView.as_view(), name='book_list'),
  url(r'^book_register/$', views.book_register, name='book_register'),
  url(r'^book_list/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
  # ex: /polls/5/results/
  url(r'^book_list/(?P<book_id>[0-9]+)/borrow/$', views.borrow, name='borrow'), 
  url(r'^book_list/(?P<book_id>[0-9]+)/return_book/$', views.return_book, name='return_book'),
]
