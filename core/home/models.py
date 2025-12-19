from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(
        max_length=100, choices=(("Male", "Male"), ("Female", "Female")), default="Male"
    )
    phone_number = models.CharField(max_length=15)
    Email = models.EmailField()
    student_bio = models.TextField()
    student_dob = models.DateField()
    student_regestration = models.DateTimeField()
    percentage = models.FloatField()
    student_image = models.ImageField(upload_to="images/students/")
    file = models.FileField(upload_to="file/students/")
    created_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()
    uid = models.UUIDField()
