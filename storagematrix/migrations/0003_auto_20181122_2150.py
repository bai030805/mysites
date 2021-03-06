# Generated by Django 2.1 on 2018-11-22 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storagematrix', '0002_auto_20181122_2143'),
    ]

    operations = [
        migrations.RenameField(
            model_name='objectstoragegeneral',
            old_name='customer',
            new_name='product_name',
        ),
        migrations.RenameField(
            model_name='objectstoragegeneral',
            old_name='ase',
            new_name='vendor',
        ),
        migrations.RemoveField(
            model_name='objectstoragegeneral',
            name='ase_manager',
        ),
        migrations.RemoveField(
            model_name='objectstoragegeneral',
            name='dcse',
        ),
        migrations.RemoveField(
            model_name='objectstoragegeneral',
            name='dcse_manager',
        ),
        migrations.RemoveField(
            model_name='objectstoragegeneral',
            name='sales_division',
        ),
        migrations.RemoveField(
            model_name='objectstoragegeneral',
            name='sales_team',
        ),
        migrations.RemoveField(
            model_name='objectstoragegeneral',
            name='uds_sales',
        ),
    ]
