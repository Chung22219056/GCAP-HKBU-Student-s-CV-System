# Generated by Django 4.1.7 on 2023-08-05 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0011_rename_test1_student_test1s_alter_cvinfobase_cvid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='test1s',
            new_name='test1',
        ),
        migrations.AlterField(
            model_name='cvinfobase',
            name='cvId',
            field=models.CharField(default='88354-CV', max_length=255),
        ),
    ]