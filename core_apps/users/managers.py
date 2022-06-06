from multiprocessing.sharedctypes import Value
from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _

# Create your tests here.
class CustomUserManager(BaseUserManager):
    def email_validator(self, email):
        try:
            validate_email(email)
        except ValidationError:
            raise ValueError(_("Need to provide valid email address"))
        
    def create_user(self, username, first_name, last_name, email, password, **extra_fields):
        if not username:
            raise ValueError(_("Need username"))
        if not first_name or not last_name:
            raise ValueError(_("Need full name"))
    
        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_("Need an email"))
        
        user = self.model(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            **extra_fields
        )
        
        user.set_password(password)
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, first_name, last_name, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        
        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superusers must have is_staff = True"))

        if not password:
            raise ValueError(_("Superusers must have password"))
        
        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_("Admin: Need an email"))
        
        user = self.create_user(username, first_name, last_name, email, password, **extra_fields)
        user.save(using=self._db)
        return user