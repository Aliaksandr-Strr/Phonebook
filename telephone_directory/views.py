from rest_framework.mixins import CreateModelMixin
from rest_framework.generics import GenericAPIView
from rest_framework.generics import get_object_or_404
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin

from .models import Contact, Person
from .serializers import ContactSerializer, PersonSerializer


class PersonView(CreateModelMixin, GenericAPIView, ListModelMixin):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ContactView(CreateModelMixin, GenericAPIView, ListModelMixin):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def perform_create(self, serializer):
        person = get_object_or_404(Person, id=self.request.data.get('person_id'))
        return serializer.save(person=person)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class SingleContactView(RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class SinglePersonView(RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
