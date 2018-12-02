from django.shortcuts import render,redirect
from projecttracking import models
from django.utils import timezone
from storagematrix import models

# Create your views here.

def objectstoragematrix(request):
    general = models.ObjectstorageGeneral.objects.all()
    interface = models.ObjectstorageInterface.objects.all()
    scalability = models.ObjectstorageScalability.objects.all()
    dataavailability = models.ObjectstorageDataAvailability.objects.all()
    dataservice = models.ObjectstorageDataService.objects.all()
    accesssecurity = models.ObjectstorageAccessSecurity.objects.all()
    ecosystem = models.ObjectstorageEcosystem.objects.all()
    operation = models.ObjectstorageOperation.objects.all()
    hardwarespec = models.ObjectstorageHardwareSpec.objects.all()
    return render(request, 'objectstoragematrix.html', {"ObjectstorageGeneral": general,
                                                        "ObjectstorageInterface": interface,
                                                        "ObjectstorageScalability": scalability,
                                                        "ObjectstorageDataAvailability": dataavailability,
                                                        "ObjectstorageDataService": dataservice,
                                                        "ObjectstorageAccessSecurity": accesssecurity,
                                                        "ObjectstorageEcosystem": ecosystem,
                                                        "ObjectstorageOperation": operation,
                                                        "ObjectstorageHardwarespec": hardwarespec,
                                                        })


