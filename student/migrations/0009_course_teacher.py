# Generated by Django 4.0 on 2022-02-28 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_remove_teacher_facebook_remove_teacher_image_and_more'),
        ('student', '0008_question_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.teacher'),
            preserve_default=False,
        ),
    ]
