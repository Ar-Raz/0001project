from django.db import models
from django.db.models.signals import pre_save, post_save

from website.utils import unique_slug_generator
from core.models import MetaTagsBase

from ckeditor_uploader.fields import RichTextUploadingField

class MotherCategory(MetaTagsBase, models.Model):
    title = models.CharField(max_length=64)
    seo_post = RichTextUploadingField()
    slug = models.SlugField(blank=True, null=True, allow_unicode=True)

    def __str__(self):
        return self.title

class MainCategory(MetaTagsBase, models.Model):
    mother_category = models.ForeignKey(MotherCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    seo_post = RichTextUploadingField()
    slug = models.SlugField(blank=True, null=True, allow_unicode=True)


    def __str__(self):
        return self.title



class Category(MetaTagsBase, models.Model):
    title = models.CharField(max_length=64)
    sub_category_of = models.ForeignKey('MainCategory', on_delete=models.CASCADE)
    seo_post = RichTextUploadingField()
    slug = models.SlugField(blank=True, null=True, allow_unicode=True)

    def __str__(self):
        return self.title



class Variation(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)  # size , round per meter


    class Meta:
        unique_together = (
            ('category', 'name')
        )

    def __str__(self):
        return self.name


class CategoryVariation(models.Model):
    variation = models.ForeignKey(Variation, on_delete=models.CASCADE, default=1)
    value = models.CharField(max_length=50, null=True, blank=True)  # S, M, L
    attachment = models.ImageField(blank=True, null=True)
    selectable = models.BooleanField(default=False, blank=True, null=True)
    yes_or_no = models.BooleanField(default=False, blank=True, null=True)

    class Meta:
        unique_together = (
            ('variation', 'value')
        )

    def __str__(self):
        return self.value

class FAQMainCategory(models.Model):
    question = models.CharField(max_length=2048)
    text = models.TextField()
    main_category = models.ForeignKey('MainCategory', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.question} for :{self.main_category.title} main category"

class FAQCategory(models.Model):
    question = models.CharField(max_length=2048)
    text = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.question} for :{self.category.title} category"

def category_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)



def main_category_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(category_pre_save_receiver, sender=Category)
pre_save.connect(main_category_pre_save_receiver, sender=MainCategory)
