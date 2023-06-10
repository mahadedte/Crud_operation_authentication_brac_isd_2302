from django.db import models


# Create your models here.

class p_info(models.Model):
    f_name = models.CharField(max_length=20, null=True, blank=True)
    l_name = models.CharField(max_length=20, null=True, blank=True)
    user_name = models.CharField(max_length=20, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    password = models.CharField(max_length=50, null=True, blank=True)
    gender = models.CharField(max_length=20)
    image = models.ImageField(upload_to='p_info/', default='default/default.jpg', max_length=50, null=False)
    t_area = models.CharField(max_length=500)

    def __str__(self):
        return str(self.email)


class prof(models.Model):
    first_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=30, blank=True, null=True)
    password = models.CharField(max_length=20, blank=True, null=True)

    # gender_choice = (
    #     ('male', 'male'),
    #     ('female', 'female'),
    #     ('others', 'others'),
    # )
    # gender = models.CharField(choices=gender_choice, max_length=20)

    gender = models.CharField(max_length=20)
    image = models.ImageField(upload_to='profile_pic/', default='default/default.jpg', blank=True, null=True)

    def __str__(self):
        return str(self.last_name)
