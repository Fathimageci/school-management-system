from django.urls import path
from .views import*

urlpatterns = [
    # Student URLs
    path('students/', StudentListCreateView.as_view(), name='student-list-create'),
    path('students/<int:pk>/', StudentRetrieveUpdateDeleteView.as_view(), name='student-detail'),
    
    #Library History
    path('library-history/', LibraryHistoryListCreateView.as_view(), name='library-history-list-create'),
    path('library-history/<int:pk>/', LibraryHistoryDetailView.as_view(), name='library-history-detail'),

    # Fee History URLs
    path('fees-history/', FeesHistoryListCreateView.as_view(), name='fees-history-list-create'),
    path('fees-history/<int:pk>/', FeesHistoryDetailView.as_view(), name='fees-history-detail'),

    #librarian creation
    # Librarian URLs
    path('librarians/', LibrarianListCreateView.as_view(), name='librarian-list-create'),
    path('librarians/<int:pk>/', LibrarianDetailView.as_view(), name='librarian-detail'),

    #Office staff creation
    # Office Staff URLs
    path('office-staff/', OfficeStaffListCreateView.as_view(), name='office-staff-list-create'),
    path('office-staff/<int:pk>/', OfficeStaffDetailView.as_view(), name='office-staff-detail'),



]
