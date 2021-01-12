from django.db import models
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin,UserManager
from cloudinary.models import CloudinaryField

@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "{}?token={}".format(
        reverse('password_reset:reset-password-request'), reset_password_token.key)

    send_mail(
        # title:
        "Password Reset for {title}".format(title="Some website title"),
        # message:
        email_plaintext_message,
        # from:
        "noreply@somehost.local",
        # to:
        [reset_password_token.user.email]
    )


class UserManager(BaseUserManager):

    def create_user(self, email, password = None,username=None, is_active=True,is_doctor=False,is_patient=False,is_superuser=False,is_staff=False,is_admin=False):
        if email is None:
            raise TypeError('Users must have email address')
        if password is None:
            raise TypeError('Users must have password')
        user = self.model(
            email=self.normalize_email(email)
        )
        
        user.set_password(password)
        user.is_active = is_active
        user.is_patient = False
        user.is_superuser = is_superuser
        user.is_staff = is_staff
       
        user.save(using=self._db)
        return user

    def create_superuser(self, email,username=None, password=None):

        user = self.create_user(
            email,
            password=password,
            username = username,
            is_staff=True,
            is_admin=True,
            is_superuser=True,
            is_patient=False
        )
        user.save()
        print(user)
        return user

    def create_doctor(self,email,username=None,password=None):
        user = self.create_user(
            email,
            password = password,
            username = username,
            is_staff = True,
            is_doctor = True
        )
        return user

    def create_patient(self,email,username=None,password=None):
        user = self.create_user(
            email,
            password = password,
            username = username,
            is_patient = True
        )  

GENDER = (
    ('M',"Male"),
    ('F',"Female"),

)

class User(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=20, unique=False)
    image = CloudinaryField('image')
    gender = models.CharField(choices=GENDER,max_length=1)
    age = models.IntegerField(default=0)
    date_joined = models.DateTimeField(
        verbose_name="date-joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last-login", auto_now=True)
    is_doctor = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects= UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = ('user')
        verbose_name_plural = ('users')

    def __str_(self):
        return self.email



class Appointment(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=255)
    date = models.DateTimeField(auto_now_add=True, blank=True)

class Responses(models.Model):
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='doctor')
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patient')
    feedback = models.TextField(max_length=255)
    date = models.DateTimeField(auto_now_add=True, blank=True)

class Services(models.Model):
    doctor = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=255)
    type = models.CharField(max_length=100)
    
    