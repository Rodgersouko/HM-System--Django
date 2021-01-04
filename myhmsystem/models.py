from django.db import models
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


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


class MyUserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Users must have email address')
        if not username:
            raise ValueError('Users must have username')
        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=False)
    date_joined = models.DateTimeField(
        verbose_name="date-joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last-login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = MyUserManager()

    def __str_(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class Doctor(models.Model):
    #Appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    speciality = models.CharField(max_length=100)
    # email = models.EmailField(verbose_name="email", max_length=60)

    def __str_(self):
        return self.doctor_speciality + '_' + self.name


class Patient(models.Model):
    Doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=100)
    disease = models.CharField(max_length=100)


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    description = models.TextField(max_length=255)
    date = models.DateTimeField(auto_now_add=True, blank=True)

class Services(models.Model):
    Doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    description = models.TextField(max_length=255)
    type = models.CharField(max_length=100)
    
    
