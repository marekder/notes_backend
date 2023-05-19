from .views import NotesView, NoteDetails
from django.urls import path

urlpatterns = [path('notes/', NotesView.as_view(), name='notes_view'),
               path('notes/<int:pk>/', NoteDetails.as_view(), name='note_details'), ]
