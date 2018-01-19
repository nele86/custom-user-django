from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, full_name, type_of_user, password=None):
        if not email:
            raise ValueError('Users must have email address')
        if not password:
            raise ValueError('User mast have password')
        if not full_name:
            raise ValueError('User mast have fullname')
        if not type_of_user:
            raise ValueError('User mast choose type')

        user = self.model(
            email=self.normalize_email(email),
            full_name=full_name,
            type_of_user=type_of_user
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def regular_user(self, email, full_name, type_of_user, password):
        user = self.create_user(
            email,
            full_name,
            type_of_user,
            password=password,
        )

        user.staff = False
        user.admin = False
        user.active = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, full_name, type_of_user, password):
        user = self.create_user(
            email,
            full_name,
            type_of_user,
            password=password,
        )

        user.staff = True
        user.admin = True
        user.active = True
        user.save(using=self._db)
        return user


# Create your models here.
# Custom User class
class User(AbstractBaseUser):
    USER_TYPE_CHOICE = (
        ('is_basic', 'Basic user'),
        ('is_expert', 'Expert user'),
    )

    email = models.EmailField(max_length=255, unique=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    type_of_user = models.CharField(max_length=10,
                                    choices=USER_TYPE_CHOICE,
                                    default='is_basic')

    # Replaces the built-in username field
    # for whatever we designate
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name', 'type_of_user']

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.full_name

    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active
