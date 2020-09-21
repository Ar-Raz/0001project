# Generated by Django 2.2 on 2020-09-21 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merchandise', '0002_miniorder'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='miniorder',
            name='approvals',
        ),
        migrations.AddField(
            model_name='miniorder',
            name='extra_discription',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='miniorder',
            name='phone_number',
            field=models.CharField(default='09191185260', max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='miniorder',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]
