# Generated by Django 4.0.2 on 2022-03-03 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0002_alter_contact_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.SmallIntegerField(choices=[(1, 'Sayt islemir'), (2, 'Menimle elaqe saxlayin')], verbose_name='Movzu'),
        ),
    ]