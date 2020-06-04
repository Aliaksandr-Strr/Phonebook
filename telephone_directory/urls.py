from django.urls import path

from .views import ContactView, PersonView,  SingleContactView, SinglePersonView

urlpatterns = [
    path('contacts/', ContactView.as_view()),
    path('person/', PersonView.as_view()),
    path('person/<int:pk>', SinglePersonView.as_view()),
    path('contacts/<int:pk>', SingleContactView.as_view())
]