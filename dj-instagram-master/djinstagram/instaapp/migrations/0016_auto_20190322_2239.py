# Generated by Django 2.1 on 2019-03-22 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instaapp', '0015_suggestion_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='suggestion',
            old_name='suggestperson',
            new_name='text',
        ),
    ]
