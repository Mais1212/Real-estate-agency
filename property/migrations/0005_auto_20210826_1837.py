# Generated by Django 2.2.20 on 2021-08-26 15:37

from django.db import migrations


def chek_for_new_building(apps, schema_editor):
    Flats = apps.get_model('property', 'Flat')
    print(Flats)

    for flat in Flats.objects.all():
        flat.new_building = flat.construction_year >= 2015
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0004_auto_20210825_1936'),
    ]

    operations = [
        migrations.RunPython(chek_for_new_building)
    ]
