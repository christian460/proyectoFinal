from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,BaseUserManager
)

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email,password=None,is_active=True,is_staff=False,is_admin=False,first_name =None,last_name=None,phone=None,gender='M',direction=None):
        if not email:
            raise ValueError("Los ususarios necesitan una Email")
         
        if not password:
            raise ValueError("Los ususarios necesitan una contraseña")

        user_obj = self.model(
            email = self.normalize_email(email)
        )
        user_obj.set_password(password)
        user_obj.first_name=first_name
        user_obj.last_name=last_name
        user_obj.phone=phone
        user_obj.gender=gender
        user_obj.direction_=direction
        user_obj.staff = is_staff
        user_obj.active= is_active
        user_obj.admin=is_admin
        user_obj.save(using=self._db)
        return user_obj
    
    def create_staffuser(self,email,password=None):
        user = self.create_user(
            email,
            password=password,
            is_staff=True
        )
        return user

    def create_superuser(self,email,password=None):
        user = self.create_user(
            email,
            password=password,
            is_staff=True,
            is_admin=True
        )
        return user

GENERO = {
    ('M','MASCULINO'),
    ('F','FEMENINO')
}

YES_NO = {
    (0,'SI'),
    (1,'NO')
}
class User(AbstractBaseUser):
    email = models.EmailField(max_length=255,unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.IntegerField(default=0)
    direction =models.CharField(max_length=100,blank=True,default= "Urb. ")
    gender = models.CharField(choices=GENERO,max_length=100)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = UserManager()
    def __str__(self):
        return self.email

    def get_first_name(self):
        return self.first_name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_active(self):
        return self.active

    @property
    def is_staff(self):
        return self.staff
    
    @property
    def is_admin(self):
        return self.admin
    


