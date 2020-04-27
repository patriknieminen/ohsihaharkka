from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from songs.models import Song

class SongList(ListView):
    model = Song

class SongView(DetailView):
    model = Song

class SongCreate(CreateView):
    model = Song
    fields = ['Song', 'Artist']
    success_url = reverse_lazy('song_list')

class SongUpdate(UpdateView):
    model = Song
    fields = ['Song', 'Artist']
    success_url = reverse_lazy('song_list')

class SongDelete(DeleteView):
    model = Song
    success_url = reverse_lazy('song_list')

class SongForm(ModelForm):
    class Meta:
        model = Song
        fields = ['song', 'artist']

def song_list(request, template_name='songs/song_list.html'):
    song = Song.objects.all()
    data = {}
    data['object_list'] = song
    return render(request, template_name, data)

def song_view(request, pk, template_name='songs/song_detail.html'):
    song= get_object_or_404(Song, pk=pk)    
    return render(request, template_name, {'object':song})

def song_create(request, template_name='songs/song_form.html'):
    form = SongForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('song_list')
    return render(request, template_name, {'form':form})

def song_update(request, pk, template_name='songs/song_form.html'):
    song= get_object_or_404(Song, pk=pk)
    form = SongForm(request.POST or None, instance=song)
    if form.is_valid():
        form.save()
        return redirect('song_list')
    return render(request, template_name, {'form':form})

def song_delete(request, pk, template_name='songs/song_confirm_delete.html'):
    song= get_object_or_404(Song, pk=pk)    
    if request.method=='POST':
        song.delete()
        return redirect('song_list')
    return render(request, template_name, {'object':song})
