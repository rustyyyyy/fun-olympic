# Generated by Django 3.2.5 on 2022-08-30 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_comment_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='update_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
