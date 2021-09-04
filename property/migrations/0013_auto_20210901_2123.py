# Generated by Django 2.2.20 on 2021-09-01 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0012_auto_20210831_2129'),
    ]

    operations = [
        migrations.RenameField(
            model_name='owner',
            old_name='owners_phonenumber',
            new_name='phonenumber',
        ),
        migrations.RenameField(
            model_name='owner',
            old_name='owner_pure_phone',
            new_name='pure_phone',
        ),
        migrations.AlterField(
            model_name='owner',
            name='apartments_in_property',
            field=models.ManyToManyField(related_name='Owner', to='property.Flat', verbose_name='Квартиры в собственности'),
        ),
    ]
