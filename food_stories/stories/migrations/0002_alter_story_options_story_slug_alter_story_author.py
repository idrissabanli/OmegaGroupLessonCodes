# Generated by Django 4.0.3 on 2022-04-28 15:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stories', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='story',
            options={'ordering': ('-created_at',)},
        ),
        migrations.AddField(
            model_name='story',
            name='slug',
            field=models.SlugField(default='slug', max_length=70),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='story',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stories', to=settings.AUTH_USER_MODEL),
        ),
    ]