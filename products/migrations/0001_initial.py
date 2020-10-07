# Generated by Django 2.2 on 2020-10-07 08:55

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import products.custom_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0001_initial'),
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=132, verbose_name='نام محصول')),
                ('price', models.FloatField(blank=True, null=True, verbose_name='قیمت محصول')),
                ('second_price', models.FloatField(blank=True, null=True, verbose_name='بازه دوم قیمت')),
                ('discount_price', models.FloatField(blank=True, null=True, verbose_name='قیمت تخفیف')),
                ('product_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('slug', models.SlugField(allow_unicode=True, blank=True, null=True)),
                ('stock', models.IntegerField(default=1, verbose_name='موجودی')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='توضیحات محصول')),
                ('minimum_order', models.CharField(blank=True, max_length=32, null=True, verbose_name='حداقل تعداد جهت سفارش')),
                ('payment_type', models.CharField(blank=True, max_length=32, null=True, verbose_name='روش پرداخت')),
                ('packing', models.CharField(blank=True, max_length=32, null=True, verbose_name='بسته بندی')),
                ('shipping', models.CharField(blank=True, max_length=32, null=True, verbose_name='نحوه ارسال')),
                ('origin', models.CharField(blank=True, max_length=32, null=True, verbose_name='اصالت کالا')),
                ('made_in', models.CharField(blank=True, max_length=32, null=True, verbose_name='تولید کشور')),
                ('delivery', models.CharField(blank=True, max_length=32, null=True, verbose_name='بازه زمانی ارسال')),
                ('samples', models.CharField(blank=True, choices=[('خیر', 'خیر'), ('رایگان', 'رایگان'), ('اعمال هزینه', 'اعمال هزینه')], max_length=24, null=True, verbose_name='ارائه نمونه')),
                ('remarks', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='ملاحظات')),
                ('label', models.CharField(blank=True, choices=[('برگزیده', 'برگزیده'), ('تخفیف', 'تخفیف'), ('پرفروش', 'پرفروش'), ('تولید داخل', 'تولید داخل'), ('شب یلدا', 'شب یلدا'), ('پیشنهاد ویژه', 'پیشنهاد ویژه')], max_length=32, null=True)),
                ('date_addded', models.DateTimeField(auto_now_add=True, null=True)),
                ('orderd_times', models.IntegerField(default=1, null=True)),
                ('short_discription', models.TextField(verbose_name='توضیحات')),
                ('category', models.ManyToManyField(to='categories.Category')),
                ('producer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.ProducerProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Variation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
            ],
            options={
                'unique_together': {('product', 'name')},
            },
        ),
        migrations.CreateModel(
            name='SliderImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('products', models.ManyToManyField(to='products.Product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_confirmed', models.BooleanField(default=False)),
                ('content', models.TextField(verbose_name='متن نظر')),
                ('username', models.CharField(blank=True, max_length=132, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product', verbose_name='محصول')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
        ),
        migrations.CreateModel(
            name='MetaDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField(default=0)),
                ('fake_content', models.CharField(max_length=1234)),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stars', products.custom_fields.IntegerRangeField(verbose_name='امتیاز')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'product')},
                'index_together': {('user', 'product')},
            },
        ),
        migrations.CreateModel(
            name='ProductVariation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=50)),
                ('attachment', models.ImageField(blank=True, upload_to='')),
                ('variation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Variation')),
            ],
            options={
                'unique_together': {('variation', 'value')},
            },
        ),
    ]
