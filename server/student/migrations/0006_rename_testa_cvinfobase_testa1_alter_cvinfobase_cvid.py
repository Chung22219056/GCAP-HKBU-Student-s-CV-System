# Generated by Django 4.2.2 on 2023-08-04 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_rename_test_cvinfobase_testa_alter_cvinfobase_cvid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cvinfobase',
            old_name='testa',
            new_name='testa1',
        ),
        migrations.AlterField(
            model_name='cvinfobase',
            name='cvId',
            field=models.CharField(default='64300-CV', max_length=255),
        ),
    ]