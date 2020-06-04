from django.db import models


class Person(models.Model):
    person = models.CharField(max_length=150, unique=True, verbose_name='ФИО')

    def __str__(self):
        return self.person

    class Meta:
        verbose_name = 'ФИО'
        verbose_name_plural = 'ФИО'
        ordering = ['person']


class Contact(models.Model):
    CONTACT_TYPES = (('home', 'Домашний телефон'), ('mobile', 'Мобильный телефон'))
    phone = models.IntegerField(unique=True, verbose_name='Телефон')
    contact_type = models.CharField(max_length=50, choices=CONTACT_TYPES, verbose_name='Тип телефона')
    person = models.ForeignKey(Person, on_delete=models.CASCADE, verbose_name='ФИО')

    class Meta:
        verbose_name = 'Телефон'
        verbose_name_plural = 'Телефоны'
