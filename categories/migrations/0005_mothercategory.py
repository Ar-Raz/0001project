# Generated by Django 2.2 on 2020-10-14 10:48

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0004_auto_20201013_1023'),
    ]

    operations = [
        migrations.CreateModel(
            name='MotherCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meta_keywords', models.CharField(blank=True, help_text='Separate keywords with commas.', max_length=255, verbose_name='Keywords')),
                ('meta_description', models.CharField(blank=True, max_length=255, verbose_name='Description')),
                ('meta_author', models.CharField(blank=True, max_length=255, verbose_name='Author')),
                ('meta_copyright', models.CharField(blank=True, max_length=255, verbose_name='Copyright')),
                ('title', models.CharField(max_length=64)),
                ('seo_post', ckeditor_uploader.fields.RichTextUploadingField()),
                ('slug', models.SlugField(allow_unicode=True, blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]