# Generated by Django 4.1 on 2022-09-01 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_client'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='link',
            field=models.TextField(default=1, verbose_name='Link'),
            preserve_default=False,
        ),
    ]
