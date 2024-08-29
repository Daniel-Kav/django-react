from django.shortcuts import render
from .models import Notes
from django.http import Http404
from django.views.generic import ListView

# Create your views here.
class NotesListView(ListView):
    model = Notes
    context_object_name = 'notes'

# def notes(request):
#     all_notes = Notes.objects.all()
#     return render(request, 'notes/notes_list.html', {'all_notes': all_notes})

def details(request, pk):
    try:
        note = Notes.objects.get(pk=pk)
    except Notes.DoesNotExist:
        raise Http404("Note Not Found")
    return render(request, 'notes/note_details.html', {'note': note})