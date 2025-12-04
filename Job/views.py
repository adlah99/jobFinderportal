from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Job

# Create your views here.
def job_lists(request):
    job_data=Job.objects.all()
    paginator = Paginator(job_data, 1)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context={'jobs':page_obj}

    return render(request,'job/job_listing.html',context)


def job_details(request,id):
    job_id=Job.objects.get(id=id)
    context={'job':job_id}
    return render(request,'job/job_details.html',context)
