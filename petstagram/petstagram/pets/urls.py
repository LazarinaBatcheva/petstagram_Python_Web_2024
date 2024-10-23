from django.urls import path, include
from petstagram.pets import views


urlpatterns = [
    path('add/', views.PetAddView.as_view(), name='pet-add'),
    path('<str:username>/pet/<slug:pet_slug>/', include([
        path('', views.PetDetailsView.as_view(), name='pet-details'),
        path('edit/', views.PetEditView.as_view(), name='pet-edit'),
        path('delete/', views.PetDeleteView.as_view(), name='pet-delete'),
    ])),
]