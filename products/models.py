from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save, post_save
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.contenttypes.fields import GenericRelation, ContentType, GenericForeignKey
from hitcount.models import HitCountMixin, HitCount
from django.dispatch import receiver

from core.models import MetaTagsBase

from tinymce.models import HTMLField
from ckeditor_uploader.fields import RichTextUploadingField

from website.utils import unique_slug_generator

from .custom_fields import IntegerRangeField
from users.models import ProducerProfile, Profile, User
from categories.models import Category , CategoryVariation


########################################################################################
"""
Notes:
1- adding tinymce for description
2- Creating the category model in the databasse
"""
########################################################################################
LABEL_CHOICES = (
    ('برگزیده','برگزیده'),
    ('تخفیف','تخفیف'),
    ('پرفروش','پرفروش'),
    ('تولید داخل','تولید داخل'),
    ('شب یلدا','شب یلدا'),
    ('پیشنهاد ویژه','پیشنهاد ویژه'),

)



class Product(MetaTagsBase ,models.Model):
    SAMPLE_CHOICES = (
        ("خیر","خیر"),
        ("رایگان","رایگان"),
        ("اعمال هزینه","اعمال هزینه"),
    )
    title = models.CharField(max_length=132, verbose_name='نام محصول')
    producer = models.ForeignKey(ProducerProfile, on_delete=models.CASCADE)
    price = models.FloatField(blank=True, null=True, verbose_name="قیمت محصول")
    second_price = models.FloatField(blank=True, null=True, verbose_name="بازه دوم قیمت")
    category = models.ManyToManyField(Category)
    discount_price = models.FloatField(blank=True, null=True, verbose_name="قیمت تخفیف")
    product_image = models.ImageField(null=True, blank=True)
    image_alt = models.CharField(max_length=225)
    slug = models.SlugField(null=True, blank=True, allow_unicode=True)
    stock = models.IntegerField(default=1, verbose_name='موجودی')
    description = RichTextUploadingField(verbose_name="توضیحات محصول")
    minimum_order = models.CharField(max_length=32, verbose_name='حداقل تعداد جهت سفارش', null=True, blank=True)
    payment_type = models.CharField(max_length=32, verbose_name='روش پرداخت', null=True, blank=True)
    packing = models.CharField(max_length=32, verbose_name="بسته بندی", null=True, blank=True)
    shipping = models.CharField(max_length=32, verbose_name="نحوه ارسال", null=True, blank=True)
    origin = models.CharField(max_length=32, verbose_name="اصالت کالا", null=True, blank=True)
    made_in = models.CharField(max_length=32, verbose_name="تولید کشور", null=True, blank=True)
    delivery = models.CharField(max_length=32, verbose_name="بازه زمانی ارسال", null=True, blank=True)
    samples = models.CharField(max_length=24, verbose_name="ارائه نمونه", null=True,
                                blank=True, choices=SAMPLE_CHOICES)
    remarks = RichTextUploadingField(verbose_name="ملاحظات", null=True, blank=True)
    label = models.CharField(max_length=32, choices=LABEL_CHOICES, null=True, blank=True)
    date_addded = models.DateTimeField(auto_now_add=True, null=True)
    orderd_times = models.IntegerField(default=1, null=True)
    short_discription = models.TextField(verbose_name="توضیحات")
    label_try = models.ManyToManyField('Label', blank=True)
    hit_count = GenericRelation(HitCount, object_id_field='object_pk',
                                        related_query_name='hit_count_generic_relation')
    is_confirmed = models.BooleanField(default=False)
    slider_images = GenericRelation('SliderImage')
    comments = GenericRelation('ProductComment')


    def __str__(self):
        return f"{self.title} by {self.producer.company_name}"



    def average_rating(self):
        sum = 0
        ratings = Rating.objects.filter(product=self)
        for rating in ratings:
            sum = sum + rating.stars
        if len(ratings) > 0:
            return sum/len(ratings)
        else:
            return 0

    @property
    def get_comments(self):
        comments = ProductComment.objects.filter(product=self, is_confirmed=True)
        return comments

    @property
    def get_sliders(self):
        sliders = SliderImage.objects.filter(product=self)
        return sliders


class SliderImage(models.Model):
    # product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField()
    content_type = models.ForeignKey(
        ContentType, on_delete=models.CASCADE,
        limit_choices_to={'model':'product'}
    )
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    def __str__(self):
        return f"{self.content_object.title} slider image"


class Label(models.Model):
    title = models.CharField(max_length=164)
    slug = models.SlugField(null=True, blank=True, allow_unicode=True)

    def __str__(self):
        return self.title

class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)  # size

    class Meta:
        unique_together = (
            ('product', 'name')
        )

    def __str__(self):
        return self.name


class ProductVariation(models.Model):
    variation = models.ForeignKey(Variation, on_delete=models.CASCADE)
    value = models.CharField(max_length=50)  # S, M, L
    attachment = models.ImageField(blank=True)

    class Meta:
        unique_together = (
            ('variation', 'value')
        )

    def __str__(self):
        return self.value


class ProductComment(models.Model):
    # product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="محصول")
    is_confirmed = models.BooleanField(default=False)
    content = models.TextField(verbose_name="متن نظر")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="کاربر" ,null=True, blank=True)
    username = models.CharField(max_length=132, null=True, blank=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    def __str__(self):
        if self.user:
            return f"{self.user.username} comment for {self.content_object.title}"
        else:
            return f"{self.username}comment for {self.content_object.title}"

class Rating(models.Model):
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  stars = IntegerRangeField(min_value=1, max_value=5, verbose_name="امتیاز")

  class Meta:
    unique_together = (('user', 'product'),)
    index_together = (('user', 'product'),)

# class ProductDetail(models.Model):
#     products = models.ManyToManyField('Product')

#     def __str__(self):
#         return self.products.all()[0].title


     

class ProductDetail(models.Model):
    products = models.ManyToManyField('Product')
    variation = models.ForeignKey(to="categories.Variation", on_delete=models.CASCADE, default=1)
    value = models.CharField(max_length=50, null=True, blank=True)  # S, M, L
    attachment = models.ImageField(blank=True, null=True)
    selectable = models.BooleanField(default=False, blank=True, null=True)
    yes_or_no = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.value

class MetaDetail(models.Model):
    count = models.PositiveIntegerField(default=0)
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fake_content = models.CharField(max_length=1234)

    def __str__(self):
        return self.product.title

@receiver(post_save, sender=Product)
def create_product_meta_detail(sender, instance=None, created=False, **kwargs):
    if created:
        MetaDetail.objects.create(product=instance, count=0, user=instance.producer.user)

def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

def label_pre_save_reciever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_receiver, sender=Product)
pre_save.connect(label_pre_save_reciever, sender=Label)
