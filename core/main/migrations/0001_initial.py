# Generated by Django 4.1 on 2022-08-31 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Indtroduceing')),
                ('about', models.TextField(verbose_name='Text')),
            ],
            options={
                'verbose_name': 'Home',
                'verbose_name_plural': 'Homes',
            },
        ),
    ]
