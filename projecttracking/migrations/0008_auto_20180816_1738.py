# Generated by Django 2.1 on 2018-08-16 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projecttracking', '0007_auto_20180816_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='customer',
            field=models.CharField(max_length=64),
        ),
    ]
