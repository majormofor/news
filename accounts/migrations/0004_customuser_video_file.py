# Generated by Django 4.2.5 on 2023-09-08 10:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0003_customuser_profile_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="video_file",
            field=models.FileField(blank=True, null=True, upload_to="video_files/"),
        ),
    ]
