# Generated by Django 2.1 on 2018-11-22 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storagematrix', '0007_objectstoragedataservice'),
    ]

    operations = [
        migrations.RenameField(
            model_name='objectstoragedataavailability',
            old_name='s3',
            new_name='erasure_code',
        ),
        migrations.RenameField(
            model_name='objectstoragescalability',
            old_name='cifs',
            new_name='max_buckets_per_cluster',
        ),
        migrations.RenameField(
            model_name='objectstoragescalability',
            old_name='hdfs',
            new_name='max_capacity_per_bucket',
        ),
        migrations.RenameField(
            model_name='objectstoragescalability',
            old_name='nfs',
            new_name='max_capacity_per_cluster',
        ),
        migrations.RenameField(
            model_name='objectstoragescalability',
            old_name='s3',
            new_name='max_nodes_per_cluster',
        ),
        migrations.RenameField(
            model_name='objectstoragescalability',
            old_name='swift',
            new_name='max_objects_per_bucket',
        ),
        migrations.AddField(
            model_name='objectstoragedataavailability',
            name='multi_copy',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='objectstoragescalability',
            name='max_objects_per_cluster',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='objectstoragescalability',
            name='max_objects_per_node',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
