# Generated by Django 4.2.5 on 2023-09-08 09:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0002_customuser_address"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="profile_image",
            field=models.ImageField(blank=True, null=True, upload_to="profile_images/"),
        ),
    ]
