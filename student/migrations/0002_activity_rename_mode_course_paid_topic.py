# Generated by Django 4.0 on 2022-01-03 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_name', models.CharField(max_length=255)),
                ('video', models.FileField(upload_to='video_activity')),
            ],
        ),
        migrations.RenameField(
            model_name='course',
            old_name='mode',
            new_name='paid',
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=300)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.course')),
            ],
        ),
    ]
