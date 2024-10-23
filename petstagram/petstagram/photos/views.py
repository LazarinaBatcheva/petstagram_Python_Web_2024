from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView
from petstagram.common.forms import CommentAddForm
from petstagram.photos.forms import PhotoAddForm, PhotoEditForm
from petstagram.photos.models import Photo


class PhotoAddView(CreateView):
    model = Photo
    form_class = PhotoAddForm
    template_name = 'photos/photo-add-page.html'
    success_url = reverse_lazy('home')


class PhotoEditView(UpdateView):
    model = Photo
    form_class = PhotoEditForm
    template_name = 'photos/photo-edit-page.html'

    def get_success_url(self):
        return reverse_lazy('photo-details', kwargs={'pk': self.object.pk})


def photo_delete_page(request, pk: int):
    Photo.objects.get(pk=pk).delete()

    return redirect('home')


class PhotoDetailView(DetailView):
    model = Photo
    template_name = 'photos/photo-details-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['likes'] = self.object.likes.all()
        context['comments'] = self.object.comments.all()
        context['comment_form'] = CommentAddForm()

        return context
