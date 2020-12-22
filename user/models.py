
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core import validators
from django.core.mail import send_mail
from django.db import models
from django.utils.translation import ugettext_lazy as _
import re


class User(AbstractBaseUser):
    username = models.CharField(_('username'), max_length=15, unique=True, help_text=_(
        'Required. 15 characters or fewer. Letters, numbers and @/./+/-/_ characters'), validators=[
        validators.RegexValidator(re.compile('^[\w.@+-]+$'), _('Enter a valid username.'), _('invalid'))])
    email = models.EmailField(_('email address'), max_length=255, unique=True)
    is_staff = models.BooleanField(_('staff status'), default=False,
                                   help_text=_('Designates whether the user can log into this admin site.'))
    is_active = models.BooleanField(_('active'), default=True, help_text=_(
        'Designates whether this user should be treated as active. Unselect this instead of deleting accounts.'))


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'email',]

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_short_name(self):
        return self.username

    def email_user(self, subject, message, from_email=None):
        send_mail(subject, message, from_email, [self.email])
