# Generated by Django 4.1.3 on 2022-12-05 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=1, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='uuid',
            field=models.UUIDField(auto_created=True, blank=True),
        ),
    ]
