# Generated by Django 4.0 on 2022-01-03 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_activity_course_activity_topic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='video',
            field=models.FileField(upload_to='video_activity/%y'),
        ),
    ]
