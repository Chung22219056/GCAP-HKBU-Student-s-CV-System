# Generated by Django 4.2.2 on 2023-08-04 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='fristName',
        ),
        migrations.RemoveField(
            model_name='student',
            name='lastName',
        ),
        migrations.AlterField(
            model_name='cvinfobase',
            name='cvId',
            field=models.CharField(default='62180-CV', max_length=255),
        ),
    ]
