# Generated by Django 4.1.7 on 2023-08-05 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0015_alter_cvinfobase_cvid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cvinfobase',
            name='cvId',
            field=models.CharField(default='79605-CV', max_length=255),
        ),
    ]
