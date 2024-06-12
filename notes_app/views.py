# notes_app/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Note
from .forms import NoteForm
from django.contrib import messages

# Create your views here.

# View to display a list of all posts.
def note_list(request):
    notes = Note.objects.all()
    # Creating a context dictionary to pass data
    context = {
                'notes': notes,
                'page_title': 'List of Notes',
    }
    return render(request, 'note_list.html', context)

# View to display details of a specific post.
def note_detail(request, pk):
    note = get_object_or_404(Note, pk=pk)
    return render(request, 'note_detail.html', {'note': note})

# View to create a new post.
def note_create(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save()
            messages.success(request, 'Note created successfully!')
            return redirect('note_detail', pk=note.pk)
    else:
        form = NoteForm()
    return render(request, 'note_form.html', {'form': form})

# View to update an existing post.
def note_update(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            note = form.save()
            messages.success(request, 'Note updated successfully!')
            return redirect('note_detail', pk=note.pk)
    else:
        form = NoteForm(instance=note)
        context = {
            'form': form,
            'page_title': 'Update Note',
    }
    return render(request, 'note_form.html', context)

# View to delete an existing post
def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        note.delete()
        messages.success(request, 'Note deleted successfully!')
        return redirect('notes_list')
    context = {
        'note': note,
        'page_title': 'Delete Note',
    }
    return render(request, 'note_confirm_delete.html', context)
