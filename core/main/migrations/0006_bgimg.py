# Generated by Django 4.1 on 2022-09-01 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_about2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bgimg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='media', verbose_name='Image')),
            ],
            options={
                'verbose_name': 'Bgimage',
                'verbose_name_plural': 'Bgimages',
            },
        ),
    ]
