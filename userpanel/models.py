from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import (
    object_relation_base_factory as generic_relation,
)

from users.models import User


class ProducerTicket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'is_producer' : True})
    subject = models.CharField(max_length=225, verbose_name="موضوع")
    content = models.TextField()
    priorty = models.CharField(max_length=100, verbose_name="اولویت", default="پایین")
    is_responded = models.BooleanField(default=False)
    is_fake = models.BooleanField(blank=True)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"ticker of {self.user.username}"

# class TicketReply(models.Model):
#     user = 