from django.db import models

# Create your models here.
class ObjectstorageGeneral(models.Model):
    id = models.AutoField(primary_key=True), # 自增的ID主键
    product_name = models.CharField(max_length=64, null=False, unique=True )
    vendor = models.CharField(max_length=64, null=True, unique=False)
    software_version = models.CharField(max_length=64, null=True, unique=False)
    release_date = models.CharField(max_length=64, null=True, unique=False)
    deployment_option = models.CharField(max_length=64, null=True, unique=False)
    node_type = models.CharField(max_length=64, null=True, unique=False)

class ObjectstorageInterface(models.Model):
    id = models.AutoField(primary_key=True), # 自增的ID主键
    product_id = models.ForeignKey(to="ObjectstorageGeneral", on_delete=None)
    s3 = models.CharField(max_length=64, null=True, unique=False)
    swift = models.CharField(max_length=64, null=True, unique=False)
    nfs = models.CharField(max_length=64, null=True, unique=False)
    cifs = models.CharField(max_length=64, null=True, unique=False)
    hdfs = models.CharField(max_length=64, null=True, unique=False)

class ObjectstorageScalability(models.Model):
    id = models.AutoField(primary_key=True), # 自增的ID主键
    product_id = models.ForeignKey(to="ObjectstorageGeneral", on_delete=None)
    max_capacity_per_cluster = models.CharField(max_length=64, null=True, unique=False)
    max_nodes_per_cluster = models.CharField(max_length=64, null=True, unique=False)
    max_buckets_per_cluster = models.CharField(max_length=64, null=True, unique=False)
    max_objects_per_cluster = models.CharField(max_length=64, null=True, unique=False)
    max_capacity_per_bucket = models.CharField(max_length=64, null=True, unique=False)
    max_objects_per_bucket = models.CharField(max_length=64, null=True, unique=False)
    max_objects_per_node = models.CharField(max_length=64, null=True, unique=False)

class ObjectstorageDataAvailability(models.Model):
    id = models.AutoField(primary_key=True), # 自增的ID主键
    product_id = models.ForeignKey(to="ObjectstorageGeneral", on_delete=None)
    erasure_code = models.CharField(max_length=64, null=True, unique=False)
    multi_copy = models.CharField(max_length=64, null=True, unique=False)
    disk_failure = models.CharField(max_length=64, null=True, unique=False)
    node_failure = models.CharField(max_length=64, null=True, unique=False)
    rack_failure = models.CharField(max_length=64, null=True, unique=False)
    site_failure = models.CharField(max_length=64, null=True, unique=False)


class ObjectstorageDataService(models.Model):
    id = models.AutoField(primary_key=True), # 自增的ID主键
    product_id = models.ForeignKey(to="ObjectstorageGeneral", on_delete=None)
    dedupe = models.CharField(max_length=64, null=True, unique=False)
    compression = models.CharField(max_length=64, null=True, unique=False)
    tiering_to_cloud = models.CharField(max_length=64, null=True, unique=False)
    autotiering = models.CharField(max_length=64, null=True, unique=False)
    worm = models.CharField(max_length=64, null=True, unique=False)
    versioning = models.CharField(max_length=64, null=True, unique=False)
    metadatasearch = models.CharField(max_length=64, null=True, unique=False)
    multi_sites_access = models.CharField(max_length=64, null=True, unique=False)
    cross_interface_access = models.CharField(max_length=64, null=True, unique=False)
    multi_sites_distribution = models.CharField(max_length=64, null=True, unique=False)
    access_load_balance = models.CharField(max_length=64, null=True, unique=False)

class ObjectstorageAccessSecurity(models.Model):
    id = models.AutoField(primary_key=True),  # 自增的ID主键
    product_id = models.ForeignKey(to="ObjectstorageGeneral", on_delete=None)
    acl = models.CharField(max_length=64, null=True, unique=False)
    bucket_policy = models.CharField(max_length=64, null=True, unique=False)
    user_policy = models.CharField(max_length=64, null=True, unique=False)

class ObjectstorageEcosystem(models.Model):
    id = models.AutoField(primary_key=True),  # 自增的ID主键
    product_id = models.ForeignKey(to="ObjectstorageGeneral", on_delete=None)
    isilon = models.CharField(max_length=64, null=True, unique=False)
    datadomain = models.CharField(max_length=64, null=True, unique=False)
    nbu = models.CharField(max_length=64, null=True, unique=False)

class ObjectstorageOperation(models.Model):
    id = models.AutoField(primary_key=True),  # 自增的ID主键
    product_id = models.ForeignKey(to="ObjectstorageGeneral", on_delete=None)
    installation_procedure = models.CharField(max_length=64, null=True, unique=False)
    performance_monitoring = models.CharField(max_length=64, null=True, unique=False)
    capacity_monitoring = models.CharField(max_length=64, null=True, unique=False)
    alert = models.CharField(max_length=64, null=True, unique=False)
    audit_log = models.CharField(max_length=64, null=True, unique=False)
    data_access_log = models.CharField(max_length=64, null=True, unique=False)

class ObjectstorageHardwareSpec(models.Model):
    id = models.AutoField(primary_key=True),  # 自增的ID主键
    product_id = models.ForeignKey(to="ObjectstorageGeneral", on_delete=None)
    cpu = models.TextField(null=True)
    memory = models.TextField(null=True)
    disk = models.TextField(null=True)
    network = models.TextField(null=True)

