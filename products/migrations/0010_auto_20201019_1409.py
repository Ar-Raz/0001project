# Generated by Django 2.2 on 2020-10-19 10:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
        ('products', '0009_product_is_confirmed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='label',
        ),
        migrations.AddField(
            model_name='rating',
            name='content_type',
            field=models.ForeignKey(default=1, limit_choices_to={'model': 'product'}, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rating',
            name='object_id',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='samples',
            field=models.CharField(blank=True, choices=[('خیر', '0'), ('رایگان', '1'), ('اعمال هزینه', '2 ')], max_length=24, null=True, verbose_name='ارائه نمونه'),
        ),
        migrations.AlterUniqueTogether(
            name='rating',
            unique_together={('user', 'object_id')},
        ),
        migrations.AlterIndexTogether(
            name='rating',
            index_together={('user', 'object_id')},
        ),
        migrations.RemoveField(
            model_name='rating',
            name='product',
        ),
    ]
