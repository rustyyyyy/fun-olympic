# Generated by Django 3.2.5 on 2022-09-18 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_livevideo'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='video/%y'),
        ),
    ]
