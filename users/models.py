from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from rest_framework.authtoken.models import Token

#validators
from .validators import validate_phone_number
from categories.models import Category


GENDER_CHOICE = (
    ('خانم','خانم'),
    ('آقای','آقای'),
)

ROLE_CHOICES = (
    ('خریدار','خریدار'),
    ('فروشنده', 'فروشنده'),
    ('هر دو', 'هر دو'),
)
class User(AbstractUser):
    is_producer = models.BooleanField(default=False, blank=True, null=True)
    role = models.CharField(max_length=12, choices=ROLE_CHOICES, blank=True, null=True)
    phone_number = models.CharField(null=True, blank=True, max_length=15 ,validators=[validate_phone_number], unique=True)

    def __str__(self):
        return self.username

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = User.first_name
    last_name = User.last_name
    gender = models.CharField(max_length=17, choices=GENDER_CHOICE, verbose_name="جنسیت")
    profile_picture = models.ImageField(blank=True, null=True, verbose_name='تصویر پروفایل')
    province = models.CharField(max_length=132, blank=True, null=True, verbose_name="استان")
    city = models.CharField(max_length=132, blank=True, null=True, verbose_name="شهر")
    company_name = models.CharField(max_length=132, blank=True, null=True, verbose_name="نام شرکت")
    phone_number = models.CharField(max_length=20, blank=True, null=True, validators=[validate_phone_number])
    company_address = models.TextField(blank=True, null=True, verbose_name='آدرس کارخانه یا شرکت')
    office_address = models.TextField(blank=True, null=True, verbose_name='آدرس دفتر')
    office_phone_num = models.CharField(max_length=20, null=True, blank=True, validators=[validate_phone_number], verbose_name='شماره تلفن دفتر')
    introduce_yourself = models.TextField(blank=True, null=True, verbose_name='معرفی مختصر شرکت')
    description = models.TextField(blank=True, null=True, verbose_name="توضیحات")
    date_created_at = models.DateTimeField(auto_now=True)
    web_site = models.CharField(max_length=120, null=True, blank=True, verbose_name="آدرس وبسایت")

    def __str__(self):
        return self.user.username

    # def get_absolute_url(self):
    #     return reverse('users:my_profile', kwargs={'pk': self.pk})


class ProducerProfile(Profile):
    BUSINESS_TYPE_CHOICES = (
        ('تولید کننده','تولید کننده'),
        ('پخش کننده','پخش کننده'),
        ('وارد کننده','وارد کننده'),
        ('خدمات','خدمات'),
        ('عمده فروش','عمده فروش'),
        ('بنک دار','بنک دار'),
        ('دولتی','دولتی'),
        ('متفرقه','متفرقه'),
    )
    categoty = models.ManyToManyField(Category, blank=True)
    department = models.CharField(max_length=132, blank=True, null=True, verbose_name="دپارتمان")
    job_title = models.CharField(max_length=132, blank=True, null=True, verbose_name="عنوان شغلی")
    postal_code = models.CharField(max_length=12, blank=True, null=True, verbose_name="کد پستی", validators=[validate_phone_number] )
    alternative_phone = models.CharField(max_length=15, blank=True, null=True, verbose_name="شماره اضطراری", validators=[validate_phone_number])
    fax_number = models.CharField(max_length=20, null=True, blank=True, validators=[validate_phone_number], verbose_name="فکس")
    business_type = models.CharField(max_length=20, null=True, blank=True,
                                verbose_name='زمینه کاری', choices=BUSINESS_TYPE_CHOICES)

    def __str__(self):
        return self.user.username


def userprofile_receiver(sender, instance, created, *args, **kwargs):
    if created:
        if instance.role == 'فروشنده':
            instance.is_producer=True
            userprofile = ProducerProfile.objects.create(user=instance)
        elif instance.role == 'خریدار':
            userprofile = Profile.objects.create(user=instance)
        elif instance.role == 'هر دو':
            instance.is_producer=True
            userprofile = ProducerProfile.objects.create(user=instance)
            userprofile_2 = Profile.objects.create(user=instance)

post_save.connect(userprofile_receiver, sender=User)

class TwoFactorToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.IntegerField()
    gen_time = models.DateTimeField()

    def __str__(self):
        return f"{self.user.username} token"

# class TokenTFA(models.Model):
#     code = models.CharField(max_length=6, blank=True)
#     gen_time = models.DateTimeField(blank=True)

#     def __str__(self):
#         return self.code

class TokenTFA(Token):
    code = models.CharField(max_length=6, blank=True)
    gen_time = models.DateTimeField(blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        TokenTFA.objects.create(user=instance, gen_time=timezone.now())
