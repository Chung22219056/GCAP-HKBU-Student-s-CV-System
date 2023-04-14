# Generated by Django 4.1.7 on 2023-04-14 04:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0019_alter_cvinfobase_cvid_alter_workexperience_end_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cvinfobase',
            name='cvId',
            field=models.CharField(default='63624-CV', max_length=255),
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='end_date',
            field=models.DateField(blank=True, default=datetime.date(2023, 4, 14), null=True),
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='start_date',
            field=models.DateField(blank=True, default=datetime.date(2023, 4, 14), null=True),
        ),
    ]
