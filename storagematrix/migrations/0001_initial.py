# Generated by Django 2.1 on 2018-11-22 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Objectstorage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.CharField(max_length=64, unique=True)),
                ('ase', models.CharField(max_length=64, null=True)),
                ('ase_manager', models.CharField(max_length=64, null=True)),
                ('dcse', models.CharField(max_length=64, null=True)),
                ('dcse_manager', models.CharField(max_length=64, null=True)),
                ('uds_sales', models.CharField(max_length=64, null=True)),
                ('sales_division', models.CharField(max_length=64, null=True)),
                ('sales_team', models.CharField(max_length=64, null=True)),
            ],
        ),
    ]
