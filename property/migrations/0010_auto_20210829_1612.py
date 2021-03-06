# Generated by Django 2.2.20 on 2021-08-29 13:12

import phonenumbers
from django.db import migrations


def normalize_number(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')

    for flat in Flat.objects.all():
        owner_number = flat.owners_phonenumber
        flat.owner_pure_phone = phonenumbers.parse(
            owner_number,
            'RU'
        )
        if phonenumbers.is_possible_number(flat.owner_pure_phone):
            flat.save()


def move_backward(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')

    for flat in Flat.objects.all():
        flat.owner_pure_phone = ''
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0009_flat_owner_pure_phone'),
    ]

    operations = [
        migrations.RunPython(normalize_number, move_backward)
    ]
