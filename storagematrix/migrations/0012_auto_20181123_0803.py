# Generated by Django 2.1 on 2018-11-23 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storagematrix', '0011_auto_20181123_0802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='network',
            field=models.TextField(null=True),
        ),
    ]
