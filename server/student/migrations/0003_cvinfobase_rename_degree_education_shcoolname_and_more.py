# Generated by Django 4.1.7 on 2023-03-22 03:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_account'),
    ]

    operations = [
        migrations.CreateModel(
            name='CvInfoBase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentID', models.CharField(max_length=20)),
                ('fristName', models.CharField(max_length=255)),
                ('lastName', models.CharField(max_length=255)),
                ('nickName', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
            ],
        ),
        migrations.RenameField(
            model_name='education',
            old_name='degree',
            new_name='shcoolName',
        ),
        migrations.RemoveField(
            model_name='education',
            name='institution',
        ),
        migrations.AddField(
            model_name='language',
            name='studentID',
            field=models.CharField(default=255, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='language',
            name='studentName',
            field=models.CharField(default=255, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cvlanguage',
            name='cv',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.cvinfobase'),
        ),
        migrations.AlterField(
            model_name='cvskill',
            name='cv',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.cvinfobase'),
        ),
        migrations.AlterField(
            model_name='education',
            name='cv',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.cvinfobase'),
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='cv',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.cvinfobase'),
        ),
        migrations.DeleteModel(
            name='CV',
        ),
    ]
