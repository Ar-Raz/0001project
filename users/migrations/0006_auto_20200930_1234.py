# Generated by Django 2.2 on 2020-09-30 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_tokentfa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tokentfa',
            name='code',
            field=models.CharField(blank=True, max_length=6),
        ),
    ]