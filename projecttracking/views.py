from django.shortcuts import render,redirect
from projecttracking import models
from django.utils import timezone

# Create your views here.
def customer_list(request):
    customers = models.Customers.objects.all()
    return render(request, 'customerlist.html', {"customer_list":customers})

def project_list(request):
    projects = models.Projects.objects.all().order_by("target_date")
    return render(request, 'projectlist.html', {"project_list":projects} )

def customer_add(request):
    if request.method == "POST":
        customer_added = request.POST.get("customer", None)
        sales_division_added = request.POST.get("sales_division",None)
        sales_team_added = request.POST.get("sales_team", None)
        ase_added = request.POST.get("ase", None)
        ase_manager_added = request.POST.get("ase_manager", None)
        dcse_added = request.POST.get("dcse", None)
        uds_sales_added = request.POST.get("uds_sales", None)
        models.Customers.objects.create(
            customer = customer_added,
            ase = ase_added,
            ase_manager = ase_manager_added,
            dcse = dcse_added,
            uds_sales = uds_sales_added,
            sales_division = sales_division_added,
            sales_team = sales_team_added,
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
        capacity_added = request.POST.get("capacity", None)
        solution_added = request.POST.get("solution", None)
        revenue_added = request.POST.get("revenue", None)
        status_added = request.POST.get("status", None)
        competition_added = request.POST.get("competition", None)
        models.Projects.objects.create(
            project=project_added,
            customer_id=customer_id_added,
            target_date = target_date_added,
            solution = solution_added,
            revenue = revenue_added,
            status = status_added,
            capacity = capacity_added,
            competition = competition_added
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
    requested_id = request.GET.get("id")
    if request.method == "POST":
        customer_updated = request.POST.get("customer", None)
        sales_division_updated = request.POST.get("sales_division",None)
        sales_team_updated = request.POST.get("sales_team", None)
        ase_updated = request.POST.get("ase", None)
        ase_manager_updated = request.POST.get("ase_manager", None)
        dcse_updated = request.POST.get("dcse", None)
        uds_sales_updated = request.POST.get("uds_sales", None)
        models.Customers.objects.filter(id=requested_id).update(
            customer=customer_updated,
            ase=ase_updated,
            ase_manager=ase_manager_updated,
            dcse=dcse_updated,
            uds_sales=uds_sales_updated,
            sales_division=sales_division_updated,
            sales_team=sales_team_updated,
        )
        return redirect("/projecttracking/customerlist/")

    else:
        customer = models.Customers.objects.get(id=requested_id)
        return render(request, 'customeredit.html', {"record":customer})

def project_edit(request):
    requested_id = request.GET.get("id")
    if request.method == "POST":
        project_updated = request.POST.get("project", None)
        solution_updated = request.POST.get("solution", None)
        capacity_updated = request.POST.get("capacity", '0')
        revenue_updated = request.POST.get("revenue", '0')
        target_date_updated = request.POST.get("target_date", None)
        models.Projects.objects.filter(id=requested_id).update(
            project=project_updated,
            solution=solution_updated,
            capacity=capacity_updated,
            revenue=revenue_updated,
            target_date=target_date_updated,
        )
        return redirect("/projecttracking/projectlist/")
    else:
        project= models.Projects.objects.get(id=requested_id)
        return render(request, 'projectedit.html', {"record":project})


