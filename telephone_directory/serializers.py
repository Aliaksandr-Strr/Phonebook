from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Contact, Person


class ContactSerializer(serializers.Serializer):
    phone = serializers.CharField(validators=[UniqueValidator(queryset=Contact.objects.all())])
    contact_type = serializers.CharField(max_length=50)
    person_id = serializers.IntegerField()
    person = serializers.StringRelatedField()

    def create(self, validated_data):
        return Contact.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.phone = validated_data.get('phone', instance.phone)
        instance.contact_type = validated_data.get('contact_type', instance.contact_type)
        instance.person_id = validated_data.get('person_id', instance.person_id)
        instance.person = validated_data.get('person', instance.person)
        instance.save()
        return instance


class PersonSerializer(serializers.Serializer):
    person = serializers.CharField(max_length=150, validators=[UniqueValidator(queryset=Person.objects.all())])

    def create(self, validated_data):
        return Person.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.person = validated_data.get('person', instance.person)
        instance.save()
        return instance
