from django.db import models

from users.models import User

# Create your models here.

class NewsTellerEmails(models.Model):
    email = models.EmailField(verbose_name="ایمیل")
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             null=True, blank=True)

    def __str__(self):
        if self.user:
            return f"{self.user.username} has mailed their email as {self.email}"
        else:
            return f"{self.email} has been mailed from anonymous user"


class Document(models.Model):
    name = models.CharField(max_length=10240132, null=True ,blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class AboutUs(models.Model):
    timestamp = models.DateTimeField()
    about_us_content = models.TextField(verbose_name="درباره ما")
    about_damir_content = models.TextField(verbose_name="درباره دمیر")
    buy_from_damir = models.TextField(verbose_name="خرید از دمیر")
    sell_in_damir = models.TextField(verbose_name="فروش در دمیر")
    terms_and_conditions = models.TextField(verbose_name="قوانین و مقررات")
    privacy_and_policy = models.TextField(verbose_name="شرایط خصوصی")
    sliders = models.ImageField(null=True, blank=True)
    slider_2 = models.ImageField(null=True, blank=True)
    slider_3 = models.ImageField(null=True, blank=True)
    slider_4 = models.ImageField(null=True, blank=True)
    slider_5 = models.ImageField(null=True, blank=True)


    def __str__(self):
        return f"about us for: {self.timestamp}"
