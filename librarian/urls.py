from django.urls import path
from .views import*


urlpatterns = [
    # Student URLs
    path('students/', StudentListCreateView.as_view(), name='student-list-create'),
    #library history
    path('library-history/', LibraryHistoryListCreateView.as_view(), name='library-history-list-create'),
]