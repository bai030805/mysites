# Generated by Django 2.1 on 2018-08-18 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projecttracking', '0013_auto_20180816_2127'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='capacity',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='projects',
            name='competition',
            field=models.CharField(max_length=64, null=True),
        ),
    ]