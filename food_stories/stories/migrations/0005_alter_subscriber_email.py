# Generated by Django 4.0.3 on 2022-05-23 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0004_subscriber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriber',
            name='email',
            field=models.EmailField(max_length=50, unique=True, verbose_name='Email'),
        ),
    ]