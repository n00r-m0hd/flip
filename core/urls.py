from django.urls import path
from .views import BookListView, StudentListView

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('students/', StudentListView.as_view(), name='student-list'),
]
