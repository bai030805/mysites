# Generated by Django 2.1 on 2018-12-03 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storagematrix', '0013_delete_test'),
    ]

    operations = [
        migrations.RenameField(
            model_name='objectstoragedataservice',
            old_name='multi_sites',
            new_name='multi_sites_access',
        ),
    ]
