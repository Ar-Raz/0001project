# Generated by Django 2.2 on 2020-09-24 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20200917_1042'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='short_discription',
            field=models.TextField(default='توضیحات کوتاه', verbose_name='توضیحات'),
            preserve_default=False,
        ),
    ]