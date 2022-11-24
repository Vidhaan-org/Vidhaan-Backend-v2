from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

import choose
from vidhaan import settings 

User = settings.AUTH_USER_MODEL

class UserPermission(models.Model):
    tab_name=models.CharField(max_length=100,unique=True)
    can_operate=models.BooleanField(default=False)


class CustomUserManager(BaseUserManager):
    use_in_migrations = True
    def _create_user(self, mobile, password, **extra_fields):
        if not mobile: 
            raise ValueError("User must have mobile")
        if not password:
            raise ValueError("Password must be provided")

        user = self.model(
            mobile = mobile, 
            **extra_fields
        )
        user.set_password(password)
        user.save(using = self._db)
        return user 

    def create_user(self, mobile, password = None, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(mobile, password, **extra_fields)
    
    def create_superuser(self, mobile, password, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(mobile, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    mobile = models.CharField(unique = True, max_length = 12)
    email = models.EmailField(max_length = 20, blank = True, null = True)
    password = models.CharField(max_length = 50, null = True, blank = True)
    first_name = models.TextField(max_length = 150, null = True, blank = True)
    last_name = models.TextField(max_length = 150, null = True, blank = True)

    access_type = models.CharField(max_length = 20, choices = choose.ACCESS_TYPE, blank = True, null = True)
    permissions=models.ManyToManyField(to=UserPermission, blank=True)

    is_staff = models.BooleanField(default = False)
    is_active = models.BooleanField(default = False)
    is_superuser = models.BooleanField(default = False) 

    created_at = models.DateTimeField(auto_now_add = True, blank = True, null = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'mobile'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'CustomUser'
        verbose_name_plural = 'CustomUser'

    def __str__(self):
        return str(self.mobile)
    
    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)
    
    def f_name(self):
        return str(self.first_name)
    
    def l_name(self):
        return str(self.last_name)

    def name(self):
        name = ""
        if self.first_name: 
            name + str(self.first_name)
        if self.last_name: 
            name + str(self.last_name)
        return name 


class UserDetails(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    user_type = models.CharField(max_length = 20, choices = choose.ACCESS_TYPE, blank = True, null = True)

    gender = models.CharField(max_length=10, choices = choose.USER_GENDER, null = True, blank = True)
    pin = models.CharField(max_length=15, null = True, blank = True)
    address = models.CharField(max_length=200, null = True, blank = True)
    city = models.CharField(max_length=50, null = True, blank = True)
    district = models.CharField(max_length=50, null = True, blank = True)
    state = models.CharField(max_length=50, null = True, blank = True)
    country = models.CharField(max_length=50, null = True, blank = True)