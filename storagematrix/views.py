from django.shortcuts import render,redirect
from projecttracking import models
from django.utils import timezone
from storagematrix import models

# Create your views here.

def objectstorage_matrix(request):
    objectstorage = models.Objectstorage.objects.all()
    return render(request, 'objectstoragematrix.html', {"Objectstorage": objectstorage,})

def objectstorage_add(request):
    if request.method == "POST":
        #Object Storage General
        product_name_added = request.POST.get("product_name", None)
        vendor_added = request.POST.get("vendor", None)
        software_version_added = request.POST.get("software_version", None)
        release_date_added = request.POST.get("release_date", None)
        deployment_option_added = request.POST.get("deployment_option", None)
        node_type_added = request.POST.get("node_type", None)

        #Object Storage Interface
        s3_added = request.POST.get("s3", None)
        swift_added = request.POST.get("swift", None)
        nfs_added = request.POST.get("nfs", None)
        cifs_added = request.POST.get("cifs", None)
        hdfs_added = request.POST.get("hdfs", None)

        #Object Storage Scalability
        max_capacity_per_cluster_added = request.POST.get("max_capacity_per_cluster", None)
        max_nodes_per_cluster_added = request.POST.get("max_nodes_per_cluster", None)
        max_buckets_per_cluster_added = request.POST.get("max_buckets_per_cluster", None)
        max_objects_per_cluster_added = request.POST.get("max_objects_per_cluster", None)
        max_capacity_per_bucket_added = request.POST.get("max_capacity_per_bucket", None)
        max_objects_per_bucket_added = request.POST.get("max_objects_per_bucket", None)
        max_objects_per_node_added = request.POST.get("max_objects_per_node", None)

        #Object Storage Data Availability
        erasure_code_added = request.POST.get("erasure_code", None)
        multi_copy_added = request.POST.get("multi_copy", None)
        disk_failure_added = request.POST.get("disk_failure", None)
        node_failure_added = request.POST.get("node_failure", None)
        rack_failure_added = request.POST.get("rack_failure", None)
        site_failure_added = request.POST.get("site_failure", None)

        #Object Storage Data Service
        dedupe_added = request.POST.get("dedupe", None)
        compression_added = request.POST.get("compression", None)
        tiering_to_cloud_added = request.POST.get("tiering_to_cloud", None)
        autotiering_added = request.POST.get("autotiering", None)
        worm_added = request.POST.get("worm", None)
        versioning_added = request.POST.get("versioning", None)
        metadatasearch_added = request.POST.get("metadatasearch", None)
        multi_sites_access_added = request.POST.get("multi_sites_access", None)
        cross_interface_access_added = request.POST.get("cross_interface_access", None)
        multi_sites_distribution_added = request.POST.get("multi_sites_distribution", None)
        access_load_balance_added = request.POST.get("access_load_balance", None)

        #Object Storage Access Security
        acl_added = request.POST.get("acl", None)
        bucket_policy_added = request.POST.get("bucket_policy", None)
        user_policy_added = request.POST.get("user_policy", None)

        #Object Storage Operation
        installation_procedure_added = request.POST.get("installation_procedure", None)
        performance_monitoring_added = request.POST.get("performance_monitoring", None)
        capacity_monitoring_added = request.POST.get("capacity_monitoring", None)
        alert_added = request.POST.get("alert", None)
        audit_log_added = request.POST.get("audit_log", None)
        data_access_log_added = request.POST.get("data_access_log", None)

        #Object Storage Hardware Spec
        cpu_added = request.POST.get("cpu", None)
        memory_added = request.POST.get("memory", None)
        disk_added = request.POST.get("disk", None)
        network_added = request.POST.get("network", None)

        #Object Storage Ecosystem
        isilon_added = request.POST.get("isilon", None)
        datadomain_added = request.POST.get("datadomain", None)
        netbackup_added = request.POST.get("netbackup", None)
        enterprisevault_added = request.POST.get("enterprisevault", None)

        models.Objectstorage.objects.create(
            # Object Storage General
            product_name=product_name_added,
            vendor=vendor_added,
            software_version=software_version_added,
            release_date=release_date_added,
            deployment_option=deployment_option_added,
            node_type=node_type_added,

            # Object Storage Interface
            s3=s3_added,
            swift=swift_added,
            nfs=nfs_added,
            cifs=cifs_added,
            hdfs=hdfs_added,

            # Object Storage Scalability
            max_capacity_per_cluster=max_capacity_per_cluster_added,
            max_nodes_per_cluster=max_nodes_per_cluster_added,
            max_buckets_per_cluster=max_buckets_per_cluster_added,
            max_objects_per_cluster=max_objects_per_cluster_added,
            max_capacity_per_bucket=max_capacity_per_bucket_added,
            max_objects_per_bucket=max_objects_per_bucket_added,
            max_objects_per_node=max_objects_per_node_added,

            # Object Storage Data Availability
            erasure_code=erasure_code_added,
            multi_copy=multi_copy_added,
            disk_failure=disk_failure_added,
            node_failure=node_failure_added,
            rack_failure=rack_failure_added,
            site_failure=site_failure_added,

            # Object Storage Data Service
            dedupe=dedupe_added,
            compression=compression_added,
            tiering_to_cloud=tiering_to_cloud_added,
            autotiering=autotiering_added,
            worm=worm_added,
            versioning=versioning_added,
            metadatasearch=metadatasearch_added,
            multi_sites_access=multi_sites_access_added,
            cross_interface_access=cross_interface_access_added,
            multi_sites_distribution=multi_sites_distribution_added,
            access_load_balance=access_load_balance_added,

            # Object Storage Access Security
            acl=acl_added,
            bucket_policy=bucket_policy_added,
            user_policy=user_policy_added,

            # Object Storage Operation
            installation_procedure=installation_procedure_added,
            performance_monitoring=performance_monitoring_added,
            capacity_monitoring=capacity_monitoring_added,
            alert=alert_added,
            audit_log=audit_log_added,
            data_access_log=data_access_log_added,

            # Object Storage Hardware Spec
            cpu=cpu_added,
            memory=memory_added,
            disk=disk_added,
            network=network_added,

            # Object Storage Ecosystem
            isilon=isilon_added,
            datadomain=datadomain_added,
            netbackup=netbackup_added,
            enterprisevault=enterprisevault_added,
        )

        return render(request, 'objectstorageadd.html')
    else:
        return render(request, 'objectstorageadd.html')


def objectstorage_edit(request):
    requested_id = request.GET.get("id")
    if request.method == "POST":
        #Object Storage General
        product_name_updated = request.POST.get("product_name", None)
        vendor_updated = request.POST.get("vendor", None)
        software_version_updated = request.POST.get("software_version", None)
        release_date_updated = request.POST.get("release_date", None)
        deployment_option_updated = request.POST.get("deployment_option", None)
        node_type_updated = request.POST.get("node_type", None)

        #Object Storage Interface
        s3_updated = request.POST.get("s3", None)
        swift_updated = request.POST.get("swift", None)
        nfs_updated = request.POST.get("nfs", None)
        cifs_updated = request.POST.get("cifs", None)
        hdfs_updated = request.POST.get("hdfs", None)

        #Object Storage Scalability
        max_capacity_per_cluster_updated = request.POST.get("max_capacity_per_cluster", None)
        max_nodes_per_cluster_updated = request.POST.get("max_nodes_per_cluster", None)
        max_buckets_per_cluster_updated = request.POST.get("max_buckets_per_cluster", None)
        max_objects_per_cluster_updated = request.POST.get("max_objects_per_cluster", None)
        max_capacity_per_bucket_updated = request.POST.get("max_capacity_per_bucket", None)
        max_objects_per_bucket_updated = request.POST.get("max_objects_per_bucket", None)
        max_objects_per_node_updated = request.POST.get("max_objects_per_node", None)

        #Object Storage Data Availability
        erasure_code_updated = request.POST.get("erasure_code", None)
        multi_copy_updated = request.POST.get("multi_copy", None)
        disk_failure_updated = request.POST.get("disk_failure", None)
        node_failure_updated = request.POST.get("node_failure", None)
        rack_failure_updated = request.POST.get("rack_failure", None)
        site_failure_updated = request.POST.get("site_failure", None)

        #Object Storage Data Service
        dedupe_updated = request.POST.get("dedupe", None)
        compression_updated = request.POST.get("compression", None)
        tiering_to_cloud_updated = request.POST.get("tiering_to_cloud", None)
        autotiering_updated = request.POST.get("autotiering", None)
        worm_updated = request.POST.get("worm", None)
        versioning_updated = request.POST.get("versioning", None)
        metadatasearch_updated = request.POST.get("metadatasearch", None)
        multi_sites_access_updated = request.POST.get("multi_sites_access", None)
        cross_interface_access_updated = request.POST.get("cross_interface_access", None)
        multi_sites_distribution_updated = request.POST.get("multi_sites_distribution", None)
        access_load_balance_updated = request.POST.get("access_load_balance", None)

        #Object Storage Access Security
        acl_updated = request.POST.get("acl", None)
        bucket_policy_updated = request.POST.get("bucket_policy", None)
        user_policy_updated = request.POST.get("user_policy", None)

        #Object Storage Operation
        installation_procedure_updated = request.POST.get("installation_procedure", None)
        performance_monitoring_updated = request.POST.get("performance_monitoring", None)
        capacity_monitoring_updated = request.POST.get("capacity_monitoring", None)
        alert_updated = request.POST.get("alert", None)
        audit_log_updated = request.POST.get("audit_log", None)
        data_access_log_updated = request.POST.get("data_access_log", None)

        #Object Storage Hardware Spec
        cpu_updated = request.POST.get("cpu", None)
        memory_updated = request.POST.get("memory", None)
        disk_updated = request.POST.get("disk", None)
        network_updated = request.POST.get("network", None)

        #Object Storage Ecosystem
        isilon_updated = request.POST.get("isilon", None)
        datadomain_updated = request.POST.get("datadomain", None)
        netbackup_updated = request.POST.get("netbackup", None)
        enterprisevault_updated = request.POST.get("enterprisevault", None)

        models.Objectstorage.objects.filter(id=requested_id).update(
            # Object Storage General
            product_name=product_name_updated,
            vendor=vendor_updated,
            software_version=software_version_updated,
            release_date=release_date_updated,
            deployment_option=deployment_option_updated,
            node_type=node_type_updated,

            # Object Storage Interface
            s3=s3_updated,
            swift=swift_updated,
            nfs=nfs_updated,
            cifs=cifs_updated,
            hdfs=hdfs_updated,

            # Object Storage Scalability
            max_capacity_per_cluster=max_capacity_per_cluster_updated,
            max_nodes_per_cluster=max_nodes_per_cluster_updated,
            max_buckets_per_cluster=max_buckets_per_cluster_updated,
            max_objects_per_cluster=max_objects_per_cluster_updated,
            max_capacity_per_bucket=max_capacity_per_bucket_updated,
            max_objects_per_bucket=max_objects_per_bucket_updated,
            max_objects_per_node=max_objects_per_node_updated,

            # Object Storage Data Availability
            erasure_code=erasure_code_updated,
            multi_copy=multi_copy_updated,
            disk_failure=disk_failure_updated,
            node_failure=node_failure_updated,
            rack_failure=rack_failure_updated,
            site_failure=site_failure_updated,

            # Object Storage Data Service
            dedupe=dedupe_updated,
            compression=compression_updated,
            tiering_to_cloud=tiering_to_cloud_updated,
            autotiering=autotiering_updated,
            worm=worm_updated,
            versioning=versioning_updated,
            metadatasearch=metadatasearch_updated,
            multi_sites_access=multi_sites_access_updated,
            cross_interface_access=cross_interface_access_updated,
            multi_sites_distribution=multi_sites_distribution_updated,
            access_load_balance=access_load_balance_updated,

            # Object Storage Access Security
            acl=acl_updated,
            bucket_policy=bucket_policy_updated,
            user_policy=user_policy_updated,

            # Object Storage Operation
            installation_procedure=installation_procedure_updated,
            performance_monitoring=performance_monitoring_updated,
            capacity_monitoring=capacity_monitoring_updated,
            alert=alert_updated,
            audit_log=audit_log_updated,
            data_access_log=data_access_log_updated,

            # Object Storage Hardware Spec
            cpu=cpu_updated,
            memory=memory_updated,
            disk=disk_updated,
            network=network_updated,

            # Object Storage Ecosystem
            isilon=isilon_updated,
            datadomain=datadomain_updated,
            netbackup=netbackup_updated,
            enterprisevault=enterprisevault_updated,
        )
        return redirect("/storagematrix/objectstorage/")
    else:
        objectstorage = models.Objectstorage.objects.get(id=requested_id)
        return render(request, 'objectstorageedit.html', {"record":objectstorage})