# Generated by Django 4.1.7 on 2023-08-05 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0013_remove_student_test1_alter_cvinfobase_cvid'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='test1',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='cvinfobase',
            name='cvId',
            field=models.CharField(default='20437-CV', max_length=255),
        ),
    ]
