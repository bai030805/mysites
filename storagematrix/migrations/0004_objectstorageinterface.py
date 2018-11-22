# Generated by Django 2.1 on 2018-11-22 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storagematrix', '0003_auto_20181122_2150'),
    ]

    operations = [
        migrations.CreateModel(
            name='ObjectstorageInterface',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s3', models.CharField(max_length=64, null=True)),
                ('swift', models.CharField(max_length=64, null=True)),
                ('nfs', models.CharField(max_length=64, null=True)),
                ('cifs', models.CharField(max_length=64, null=True)),
                ('hdfs', models.CharField(max_length=64, null=True)),
                ('product_id', models.ForeignKey(on_delete=None, to='storagematrix.ObjectstorageGeneral')),
            ],
        ),
    ]
