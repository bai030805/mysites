from django.db import models

# Create your models here.
class Customers(models.Model):
    id = models.AutoField(primary_key=True), # 自增的ID主键
    customer = models.CharField(max_length=64, null=False, unique=True )
    ase = models.CharField(max_length=64, null=True, unique=False)
    ase_manager = models.CharField(max_length=64, null=True, unique=False)
    dcse = models.CharField(max_length=64, null=True, unique=False)
    dcse_manager = models.CharField(max_length=64, null=True, unique=False)
    uds_sales = models.CharField(max_length=64, null=True, unique=False)

class Projects(models.Model):
    id = models.AutoField(primary_key=True),  # 自增的ID主键
    project = models.CharField(max_length=64, null=False, unique=False)
    customer_id = models.ForeignKey(to="Customers", on_delete=None)
    solution = models.CharField(max_length=64, null=True, unique=False)
    revenue = models.IntegerField(null=True)
    target_date = models.CharField(max_length=64, null=True, unique=False)
    status = models.CharField(max_length=64, null=True, unique=False)


class Activities(models.Model):
    id = models.AutoField(primary_key=True), # 自增的ID主键
    project_id = models.ForeignKey(to="Projects",on_delete=None)
    customer_id = models.ForeignKey(to="Customers",on_delete=None)
    activity_content = models.TextField(null=True)
    next_step = models.TextField(null=True)
    project_status = models.CharField(max_length=64, null=True, unique=False)
    update_date = models.DateTimeField()
