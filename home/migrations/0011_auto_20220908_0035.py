# Generated by Django 3.2.5 on 2022-09-08 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20220908_0033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='time',
            field=models.TimeField(),
        ),
    ]