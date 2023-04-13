from django.db import models

state_choices = (("Andhra Pradesh", "Andhra Pradesh"), ("Arunachal Pradesh ", "Arunachal Pradesh "), ("Assam", "Assam"), ("Bihar", "Bihar"), ("Chhattisgarh", "Chhattisgarh"), ("Goa", "Goa"), ("Gujarat", "Gujarat"), ("Haryana", "Haryana"), ("Himachal Pradesh", "Himachal Pradesh"), ("Jammu and Kashmir ", "Jammu and Kashmir "), ("Jharkhand", "Jharkhand"), ("Karnataka", "Karnataka"), ("Kerala", "Kerala"), ("Madhya Pradesh", "Madhya Pradesh"), ("Maharashtra", "Maharashtra"), ("Manipur", "Manipur"), ("Meghalaya", "Meghalaya"), ("Mizoram", "Mizoram"), ("Nagaland", "Nagaland"), ("Odisha", "Odisha"),
                 ("Punjab", "Punjab"), ("Rajasthan", "Rajasthan"), ("Sikkim", "Sikkim"), ("Tamil Nadu", "Tamil Nadu"), ("Telangana", "Telangana"), ("Tripura", "Tripura"), ("Uttar Pradesh", "Uttar Pradesh"), ("Uttarakhand", "Uttarakhand"), ("West Bengal", "West Bengal"), ("Andaman and Nicobar Islands", "Andaman and Nicobar Islands"), ("Chandigarh", "Chandigarh"), ("Dadra and Nagar Haveli", "Dadra and Nagar Haveli"), ("Daman and Diu", "Daman and Diu"), ("Lakshadweep", "Lakshadweep"), ("National Capital Territory of Delhi", "National Capital Territory of Delhi"), ("Puducherry", "Puducherry"))
# Create your models here.


class Resume(models.Model):
    name = models.CharField(max_length=20)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    gender = models.CharField(max_length=10)
    locality = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    pin = models.PositiveIntegerField()
    state = models.CharField(choices=state_choices,max_length=255, null=True, blank=True)
    mobile = models.PositiveIntegerField()
    email = models.EmailField(max_length=100)
    job_city = models.CharField(max_length=50)
    profile_pic = models.ImageField(upload_to='profilepic', blank=True)
    my_file = models.FileField(upload_to='doc', blank=True)
