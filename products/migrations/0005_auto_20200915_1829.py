# Generated by Django 2.2 on 2020-09-15 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_date_addded'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='orderd_times',
            field=models.IntegerField(default=1, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='date_addded',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
