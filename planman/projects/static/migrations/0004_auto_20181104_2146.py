# Generated by Django 2.1.3 on 2018-11-05 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20181104_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(blank=True, default='Untitled project ', max_length=200),
        ),
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.CharField(blank=True, default='Untitled task ', max_length=200),
        ),
    ]
