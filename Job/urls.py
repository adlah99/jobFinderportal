from django.urls import path
from . import views
app_name= 'Job'

urlpatterns = [
    path('',views.job_lists ),
    path('<str:slug>',views.job_details,name='jobs_details'),
]
