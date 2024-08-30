from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Notes
from django.http import Http404
from django.views.generic import ListView,DetailView, CreateView,UpdateView, DeleteView
from .forms import NotesForm

# Create your views here.
class NotesListView(ListView):
    model = Notes
    context_object_name = 'all_notes'
    template_name = 'notes/notes_list.html'

# def notes(request):
#     all_notes = Notes.objects.all()
#     return render(request, 'notes/notes_list.html', {'all_notes': all_notes})

class DetailsView(DetailView):
    model = Notes
    context_object_name = 'note'
    template_name='notes/note_details.html'

# def details(request, pk):
#     try:
#         note = Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         raise Http404("Note Not Found")
#     return render(request, 'notes/note_details.html', {'note': note})



class NotesCreateView(CreateView):
    model = Notes
    success_url = reverse_lazy('notes.list')
    form_class = NotesForm

class NotesUpdateView(UpdateView):
    model = Notes
    success_url = reverse_lazy('notes.list')
    form_class = NotesForm
