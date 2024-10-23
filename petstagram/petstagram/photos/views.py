from django.shortcuts import render, redirect
from petstagram.photos.forms import PhotoAddForm, PhotoEditForm
from petstagram.photos.models import Photo


def photo_add_page(request):
    form = PhotoAddForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('home')

    context = {
        'form': form,
    }

    return render(request, 'photos/photo-add-page.html', context)


def photo_edit_page(request, pk: int):
    photo = Photo.objects.get(pk=pk)
    form = PhotoEditForm(request.POST or None, instance=photo)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('photo-details', pk)

    context = {
        'photo': photo,
        'form': form,
    }

    return render(request, 'photos/photo-edit-page.html', context)


def photo_delete_page(request, pk: int):
    Photo.objects.get(pk=pk).delete()

    return redirect('home')



def photo_details_page(request, pk: int):
    photo = Photo.objects.get(pk=pk)
    likes = photo.likes.all()
    comments = photo.comments.all()

    comment_form = CommentAddForm()

    context = {
        'photo': photo,
        'likes': likes,
        'comments': comments,
        'comment_form': comment_form,
    }

    return render(request, 'photos/photo-details-page.html', context)
