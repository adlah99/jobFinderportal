from django.db import models
from django.utils.text import slugify

# Create your models here.
'''django model field :
    - html widgth
    - validation
    - db size
'''
def image_upload(instance,filename):
    imagename,extension=filename.split(".")
    return "jobs/%s.%s"%(instance.id,extension)
class Category(models.Model):
    name = models.CharField(max_length=15)
    def __str__(self) :
        return self.name
    class Meta:
        
        verbose_name_plural = 'categories'
class Job(models.Model):
    Job_type = (
        ('full time','full time'),
        ('part time','part time'),
        ('Remote','Remote'),
        ('Freelance','Freelance'),
    )
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    required = models.TextField(max_length=1000)
    experience = models.IntegerField(default=1)
    price = models.IntegerField(default=0)
    posted_date = models.DateTimeField(auto_now=True)
    application_date= models.DateTimeField(auto_now=True)
    Vacancy = models.IntegerField(default=1)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    job_type = models.CharField(max_length=15, choices=Job_type)
    job_image = models.ImageField(upload_to=image_upload )
    slug = models.SlugField(blank=True, null=True)
    def save(self,*args,**kwargs) :
        self.slug = slugify(self.title)

        super(Job,self).save(*args,**kwargs)

    def __str__(self) :
        return self.title
class JobApplication(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    resume = models.FileField(upload_to='resumes/')
    cover_letter = models.TextField(max_length=500)
    applied_at = models.DateTimeField(auto_now_add=True)
    def __str__(self) :
        return self.name

