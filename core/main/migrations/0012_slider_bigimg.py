# Generated by Django 4.1 on 2022-09-01 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_rename_about2_slider_about_rename_name_slider_name1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='bigimg',
            field=models.ImageField(default=1, upload_to='media', verbose_name='BigImage'),
            preserve_default=False,
        ),
    ]
