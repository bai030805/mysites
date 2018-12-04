from django.shortcuts import render,redirect
from projecttracking import models
from django.utils import timezone
from storagematrix import models

# Create your views here.

def objectstorage_matrix(request):
    objectstorage = models.Objectstorage.objects.all()
#    general = models.ObjectstorageGeneral.objects.all()
#    interface = models.ObjectstorageInterface.objects.all()
#    scalability = models.ObjectstorageScalability.objects.all()
#    dataavailability = models.ObjectstorageDataAvailability.objects.all()
#    dataservice = models.ObjectstorageDataService.objects.all()
#    accesssecurity = models.ObjectstorageAccessSecurity.objects.all()
#    ecosystem = models.ObjectstorageEcosystem.objects.all()
#    operation = models.ObjectstorageOperation.objects.all()
#    hardwarespec = models.ObjectstorageHardwareSpec.objects.all()
    return render(request, 'objectstoragematrix.html', {"Objectstorage": objectstorage,
                                                        #"ObjectstorageGeneral": general,
                                                        #"ObjectstorageInterface": interface,
                                                        #"ObjectstorageScalability": scalability,
                                                        #"ObjectstorageDataAvailability": dataavailability,
                                                        #"ObjectstorageDataService": dataservice,
                                                        #"ObjectstorageAccessSecurity": accesssecurity,
                                                        #"ObjectstorageEcosystem": ecosystem,
                                                        #"ObjectstorageOperation": operation,
                                                        #"ObjectstorageHardwarespec": hardwarespec,
                                                        })

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
        erasure_code_added = request.POST.get("erasure_cod", None)
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
        nbu_added = request.POST.get("nbu", None)

        models.Customers.objects.create(
            customer = customer_added,
            ase = ase_added,
            ase_manager = ase_manager_added,
            dcse = dcse_added,
            uds_sales = uds_sales_added,
            sales_division = sales_division_added,
            sales_team = sales_team_added,
        )

        return render(request, 'objectstoragematrix.html')
    else:
        return render(request, 'objectstorageadd.html')

