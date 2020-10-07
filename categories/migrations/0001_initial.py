# Generated by Django 2.2 on 2020-10-07 08:54

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('seo_post', ckeditor_uploader.fields.RichTextUploadingField()),
                ('slug', models.SlugField(allow_unicode=True, blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MainCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('seo_post', ckeditor_uploader.fields.RichTextUploadingField()),
                ('slug', models.SlugField(allow_unicode=True, blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Variation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories.Category')),
            ],
            options={
                'unique_together': {('category', 'name')},
            },
        ),
        migrations.CreateModel(
            name='FAQMainCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=2048)),
                ('text', models.TextField()),
                ('main_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories.MainCategory')),
            ],
        ),
        migrations.CreateModel(
            name='FAQCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=2048)),
                ('text', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories.Category')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='sub_category_of',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories.MainCategory'),
        ),
        migrations.CreateModel(
            name='CategoryVariation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(blank=True, max_length=50, null=True)),
                ('attachment', models.ImageField(blank=True, null=True, upload_to='')),
                ('selectable', models.BooleanField(blank=True, default=False, null=True)),
                ('yes_or_no', models.BooleanField(blank=True, default=False, null=True)),
                ('variation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories.Variation')),
            ],
            options={
                'unique_together': {('variation', 'value')},
            },
        ),
    ]
