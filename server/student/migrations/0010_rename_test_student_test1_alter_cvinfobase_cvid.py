# Generated by Django 4.1.7 on 2023-08-05 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0009_student_test_alter_cvinfobase_cvid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='test',
            new_name='test1',
        ),
        migrations.AlterField(
            model_name='cvinfobase',
            name='cvId',
            field=models.CharField(default='18295-CV', max_length=255),
        ),
    ]