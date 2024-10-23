from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from petstagram.common.forms import CommentAddForm
from petstagram.pets.forms import PetAddForm, PetEditForm, PetDeleteForm
from petstagram.pets.models import Pet


class PetAddView(CreateView):
    model = Pet
    form_class = PetAddForm
    template_name = 'pets/pet-add-page.html'
    success_url = reverse_lazy('profile-details', kwargs={'pk': 1})


class PetEditView(UpdateView):
    model = Pet
    form_class = PetEditForm
    template_name = 'pets/pet-edit-page.html'
    slug_url_kwarg = 'pet_slug'
    context_object_name = 'pet'

    def get_success_url(self):
        return reverse_lazy(
            'pet-details',
            kwargs={
                'username': self.kwargs['username'],
                'pet_slug': self.kwargs['pet_slug'],
            }
        )


class PetDeleteView(DeleteView):
    model = Pet
    form_class = PetDeleteForm
    template_name = 'pets/pet-delete-page.html'
    context_object_name = 'pet'
    slug_url_kwarg = 'pet_slug'
    success_url = reverse_lazy('profile-details', kwargs={'pk': 1})

    def get_initial(self):
        return self.get_object().__dict__


class PetDetailsView(DetailView):
    model = Pet
    template_name = 'pets/pet-details-page.html'
    context_object_name = 'pet'
    slug_url_kwarg = 'pet_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['all_photos'] = self.object.tagged_pets_photos.all()
        context['comment_form'] = CommentAddForm()

        return context
