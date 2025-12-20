from time import timezone
from django.db import models
from django.forms import IntegerField


class Department(models.Model):
    department_name = models.CharField(max_length=100)
    

# Create your models here.
class Student(models.Model):
    # department = models.ForeignKey(Department, models.SET_NULL,models.CASCADE,models.SET_DEFAULT,models.PROTECT)
    # department = models.OneToOneField(Department, models.SET_NULL,models.CASCADE,models.SET_DEFAULT,models.PROTECT)
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
    # student_image = models.ImageField(upload_to="images/students/")
    # file = models.FileField(upload_to="file/students/")
    created_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now_add=True)
    # slug = models.SlugField()
    # uid = models.UUIDField()


# student = Student.objects.create(
#     name = "Bruce",
#     age = "21",
#     phone_number = "09876543231",
#     Email = "Bruce@gmail.com",
#     student_bio ="hi i'm batman",
#     student_regestration = timezone.now(),
#     percentage = 9.00,
#     student_dob="1995-05-25"
# )



# student = Student.objects.create(
#     name = "Rakshita",
#     age = 23,
#     phone_number = "2345678901",
#     gender = "female",
#     Email = "rakshita@gmail.com",
#     student_bio ="Hi I'm Actor",
#     student_regestration = timezone.now(),
#     percentage = 10,
#     student_dob="1998-01-23"
# )
