# Generated by Django 2.2 on 2020-09-30 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200930_0904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='twofactortoken',
            name='gen_time',
            field=models.DateTimeField(),
        ),
    ]