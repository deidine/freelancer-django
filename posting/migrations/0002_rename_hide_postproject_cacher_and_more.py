# Generated by Django 4.0 on 2024-01-14 20:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posting', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postproject',
            old_name='hide',
            new_name='cacher',
        ),
        migrations.RenameField(
            model_name='postproject',
            old_name='description_project',
            new_name='description_projet',
        ),
        migrations.RenameField(
            model_name='postproject',
            old_name='name_project',
            new_name='nom_projet',
        ),
        migrations.RenameField(
            model_name='postproject',
            old_name='end_price',
            new_name='prix_derniere',
        ),
        migrations.RenameField(
            model_name='postproject',
            old_name='start_price',
            new_name='prix_premiere',
        ),
    ]