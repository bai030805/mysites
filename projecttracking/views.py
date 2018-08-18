from django.shortcuts import render
from projecttracking import models
from django.utils import timezone

# Create your views here.
def customer_list(request):
    customers = models.Customers.objects.all()
    return render(request, 'customerlist.html', {"customer_list":customers})

def project_list(request):
    projects = models.Projects.objects.all()
    return render(request, 'projectlist.html', {"project_list":projects} )

def customer_add(request):
    if request.method == "POST":
        customer_added = request.POST.get("customer", None)
        ase_added = request.POST.get("ase", None)
        ase_manager_added = request.POST.get("ase_manager", None)
        dcse_added = request.POST.get("dcse", None)
        dcse_manager_added = request.POST.get("dcse_manager", None)
        uds_sales_added = request.POST.get("uds_sales", None)
        models.Customers.objects.create(
            customer = customer_added,
            ase = ase_added,
            ase_manager = ase_manager_added,
            dcse = dcse_added,
            dcse_manager = dcse_manager_added,
            uds_sales = uds_sales_added,
        )
        return render(request, 'customeradd.html')
    else:
        return render(request, 'customeradd.html')

def project_add(request):
    customers = models.Customers.objects.all()
    if request.method == "POST":
        project_added = request.POST.get("project", None)
        customer_id_added = models.Customers.objects.get(id=request.POST.get("customers", None))
        target_date_added = request.POST.get("target_date", None)
        solution_added = request.POST.get("solution", None)
        revenue_added = request.POST.get("revenue", None)
        status_added = request.POST.get("status", None)
        models.Projects.objects.create(
            project=project_added,
            customer_id=customer_id_added,
            target_date = target_date_added,
            solution = solution_added,
            revenue = revenue_added,
            status = status_added,
        )
        return render(request, 'projectadd.html', {"customer_list": customers})
    else:

        return render(request, 'projectadd.html', {"customer_list": customers})

def project_activities(request):
    requested_project_id = request.GET.get("id")
    related_activities = models.Activities.objects.filter(project_id=requested_project_id).order_by("update_date")
    if request.method == "POST":
        project_id_added = models.Projects.objects.get(id=requested_project_id)
        customer_id_added = models.Projects.objects.get(id=requested_project_id).customer_id
        activity_content_added = request.POST.get("activity_content", None)
        next_step_added = request.POST.get("next_step", None)
        project_status_added = request.POST.get("project_status", None)
        update_date_added = timezone.now()
        models.Activities.objects.create(
            customer_id=customer_id_added,
            project_id = project_id_added,
            activity_content = activity_content_added,
            next_step = next_step_added,
            project_status = project_status_added,
            update_date = update_date_added,
        )
        models.Projects.objects.filter(id = requested_project_id).update(status=project_status_added)
        requested_project = models.Projects.objects.get(id=requested_project_id)
        return render(request, 'projectactivities.html', {"requested_project":requested_project, "activity_list": related_activities})
    else:
        requested_project = models.Projects.objects.get(id=requested_project_id)
        return render(request, 'projectactivities.html', {"requested_project":requested_project, "activity_list": related_activities})

def customer_edit(request):
    pass

def project_edit(request):
    pass


