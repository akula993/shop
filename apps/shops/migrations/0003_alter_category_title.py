# Generated by Django 4.1.3 on 2022-12-05 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0002_category_slug_alter_category_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=50, null=True, unique=True, verbose_name='Название'),
        ),
    ]
