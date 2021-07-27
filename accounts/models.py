from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, 
    BaseUserManager,
    PermissionsMixin
)

class UserManager(BaseUserManager):
    def create_user(
        self, 
        unit, 
        password = None, 
        **extra_fields
    ):
        if not unit:
            raise ValueError('Users must have an unit')

        user = self.model(unit = unit, **extra_fields)
        user.set_password(password)
        user.save(using = self.db)

        return user

    def create_superuser(
        self,
        unit,
        password
    ):
        if not unit or not unit == "0000":
            raise ValueError('INVALID_UNIT')

        user = self.create_user(unit = unit, password = password)
        user.is_superuser = True
        user.save(using = self.db)

        return user

class User(AbstractBaseUser, PermissionsMixin):
    unit     = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    objects  = UserManager()

    USERNAME_FIELD = 'unit'

    class Meta:
        db_table = 'users'

class DoorLog(models.Model):
    open_date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'door_logs'
