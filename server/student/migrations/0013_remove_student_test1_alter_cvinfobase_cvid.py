# Generated by Django 4.1.7 on 2023-08-05 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0012_rename_test1s_student_test1_alter_cvinfobase_cvid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='test1',
        ),
        migrations.AlterField(
            model_name='cvinfobase',
            name='cvId',
            field=models.CharField(default='99683-CV', max_length=255),
        ),
    ]
