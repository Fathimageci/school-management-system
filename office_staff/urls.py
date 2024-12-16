from django.urls import path
from .views import*


urlpatterns = [
    # Student URLs
    path('students/', StudentListCreateView.as_view(), name='student-list-create'),
    #library history
    path('library-history/', LibraryHistoryListCreateView.as_view(), name='library-history-list-create'),
    #fee history
    path('fees-history/', FeesHistoryListCreateView.as_view(), name='fees-history-list-create'),
    path('fees-history/<int:pk>/', FeesHistoryDetailView.as_view(), name='fees-history-detail'),
]