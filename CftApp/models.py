from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from django.utils import timezone

class CustomUserManager(BaseUserManager):
    def _create_user(self, name, password, **extra_fields):
        """Helper function to create and save a user with the given name and password."""
        if not name:
            raise ValueError("The given name must be set")

        user = self.model(name=name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, name, password, **extra_fields):
        """Creates and saves a regular user with the given name and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(name, password, **extra_fields)
    
    def create_superuser(self, name, password, **extra_fields):
        """Creates and saves a superuser with the given name and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if not extra_fields.get('is_staff'):
            raise ValueError('Superuser must have is_staff=True.')
        if not extra_fields.get('is_superuser'):
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(name, password, **extra_fields)
    
class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = []  # List fields required during user creation other than 'name' and 'password'

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    
    def get_full_name(self):
        """Returns the full name of the user."""
        return self.name
    
    def get_short_name(self):
        """Returns the short name of the user."""
        return self.name
    
#################################################################################

