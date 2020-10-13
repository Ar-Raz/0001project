from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import (
    object_relation_base_factory as generic_relation,
)

from users.models import User


class ProduerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)